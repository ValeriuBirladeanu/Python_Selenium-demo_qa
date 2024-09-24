import allure
import requests
from base.base_page import BasePage
from config.urls import Urls


class BrokenLinksImages(BasePage):
    PAGE_URL = Urls.BROKEN_LINKS_IMAGES
    EXPECTED_VALID_IMAGE_URL = Urls.HOST + "/images/Toolsqa.jpg"
    EXPECTED_BROKEN_IMAGE_URL = Urls.HOST + "/images/Toolsqa_1.jpg"

    VALID_IMAGE = ("xpath", "//p[text()='Valid image']/following-sibling::img[@src='/images/Toolsqa.jpg']")
    BROKEN_IMAGE = ("xpath", "//img[@src='/images/Toolsqa_1.jpg']")
    VALID_LINK = ("xpath", "//a[text()='Click Here for Valid Link']")
    BROKEN_LINK = ("xpath", "//a[text()='Click Here for Broken Link']")

    CARDS_CATEGORY = ("xpath", "//div[@class='category-cards']")
    ERROR_500_MESSAGE = ("xpath", "//p[contains(text(), 'This page returned a 500 status code')]")

    @allure.step("Verify if image is valid")
    def check_valid_image(self):
        image = self.element_is_presence(self.VALID_IMAGE)
        image_src = image.get_attribute("src")
        assert image_src == self.EXPECTED_VALID_IMAGE_URL, f"Expected image URL to be '{self.EXPECTED_VALID_IMAGE_URL}', but got '{image_src}'"
        response = requests.get(image_src)
        content_type = response.headers.get('Content-Type', '')
        assert content_type in ['image/jpeg', 'image/png'], f"Expected an image but got {content_type}"

    @allure.step("Verify if image is broken")
    def check_broken_image(self):
        image = self.element_is_presence(self.BROKEN_IMAGE)
        image_src = image.get_attribute("src")
        assert image_src == self.EXPECTED_BROKEN_IMAGE_URL, f"Expected image URL to be '{self.EXPECTED_BROKEN_IMAGE_URL}', but got '{image_src}'"
        response = requests.get(image_src)
        content_type = response.headers.get('Content-Type', '')
        assert content_type not in ['image/jpeg', 'image/png'], f"Expected a non-image content but got {content_type}"

    @allure.step("Click on valid link")
    def click_valid_link(self):
        self.scroll_to(self.VALID_LINK)
        valid_link = self.element_is_clickable(self.VALID_LINK)
        valid_link_href = valid_link.get_attribute('href')
        if not valid_link_href.startswith("https://"):
            self.valid_link_href = valid_link_href.replace("http://", "https://")
        valid_link.click()

    @allure.step("Verify if link is valid")
    def check_opened_valid_link(self):
        current_url = self.driver.current_url
        expected_url = self.valid_link_href
        assert expected_url == current_url, f"Expected URL {expected_url} but it was {current_url}"
        self.element_is_presence(self.CARDS_CATEGORY)

    @allure.step("Click on broken link")
    def click_broken_link(self):
        self.scroll_to(self.BROKEN_LINK)
        self.element_is_clickable(self.BROKEN_LINK).click()

    @allure.step("Verify if link is broken")
    def check_opened_broken_link(self):
        expected_text = "This page returned a 500 status code"
        self.check_element_text(self.ERROR_500_MESSAGE, expected_text)