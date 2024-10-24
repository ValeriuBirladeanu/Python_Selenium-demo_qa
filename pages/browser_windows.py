import allure
from base.base_page import BasePage
from config.urls import Urls


class BrowserWindows(BasePage):
    PAGE_URL = Urls.BROWSER_WINDOWS

    NEW_TAB_BUTTON = ("xpath", "//button[@id='tabButton']")
    NEW_WINDOW_BUTTON = ("xpath", "//button[@id='windowButton']")
    TEXT_NEW_TAB_WINDOW = ("xpath", "//h1[@id='sampleHeading']")
    TEXT = "This is a sample page"

    @allure.step("Click new tab button")
    def click_new_tab_button(self):
        self.element_is_clickable(self.NEW_TAB_BUTTON).click()

    @allure.step("Check opened new tab")
    def check_opened_new_tab(self):
        self.wait_for_new_tab()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.check_element_text(self.TEXT_NEW_TAB_WINDOW, self.TEXT)

    @allure.step("Click new window button")
    def click_new_window_button(self):
        self.element_is_clickable(self.NEW_WINDOW_BUTTON).click()

    @allure.step("Check opened new window")
    def check_opened_new_window(self):
        self.wait_for_new_tab()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.check_element_text(self.TEXT_NEW_TAB_WINDOW, self.TEXT)