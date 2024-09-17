import allure
import requests
from base.base_page import BasePage
from config.urls import Urls


class Links(BasePage):
    PAGE_URL = Urls.Links

    SIMPLE_LINK = ("xpath", "//a[@id='simpleLink']")
    CARDS_CATEGORY = ("xpath", "//div[@class='category-cards']")

    LINKS = {
        "created": (("xpath", "//a[@id='created']"), "https://demoqa.com/created", 201,
                    "Link has responded with staus 201 and status text Created"),
        "no_content": (("xpath", "//a[@id='no-content']"), "https://demoqa.com/no-content", 204,
                       "Link has responded with staus 204 and status text No Content"),
        "moved": (("xpath", "//a[@id='moved']"), "https://demoqa.com/moved", 301,
                  "Link has responded with staus 301 and status text Moved Permanently"),
        "bad_request": (("xpath", "//a[@id='bad-request']"), "https://demoqa.com/bad-request", 400,
                        "Link has responded with staus 400 and status text Bad Request"),
        "unauthorized": (("xpath", "//a[@id='unauthorized']"), "https://demoqa.com/unauthorized", 401,
                         "Link has responded with staus 401 and status text Unauthorized"),
        "forbidden": (("xpath", "//a[@id='forbidden']"), "https://demoqa.com/forbidden", 403,
                      "Link has responded with staus 403 and status text Forbidden"),
        "not_found": (("xpath", "//a[@id='invalid-url']"), "https://demoqa.com/invalid-url", 404,
                      "Link has responded with staus 404 and status text Not Found")
    }

    RESPONSE_LOCATOR = ("xpath", "//p[@id='linkResponse']")

    @allure.step("Click on the button and switch to new tab")
    def switch_new_tab(self):
        simple_link = self.element_is_clickable(self.SIMPLE_LINK)
        self.simple_link_href = simple_link.get_attribute('href')
        simple_link.click()
        self.wait_for_new_tab()
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Check if there has been a change to another tab")
    def check_switch_new_tab(self):
        current_url = self.driver.current_url
        assert self.simple_link_href == current_url, f"Expected URL {self.simple_link_href}, but got {current_url}"
        self.element_is_presence(self.CARDS_CATEGORY)

    @allure.step("Click on the link")
    def click_link(self, link_key):
        locator, _, _, _ = self.LINKS[link_key]
        self.scroll_to(locator)
        element = self.element_is_clickable(locator)
        element.click()

    @allure.step("Verify link response and text")
    def verify_link_response_and_text(self, link_key):
        _, expected_url, expected_status_code, expected_text = self.LINKS[link_key]
        response = requests.get(expected_url)
        assert response.status_code == expected_status_code, f'Status code wrong {response.status_code}'
        self.check_element_text(self.RESPONSE_LOCATOR, expected_text)