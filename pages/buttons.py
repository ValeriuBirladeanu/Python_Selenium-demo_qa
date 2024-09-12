import allure
from base.base_page import BasePage
from config.links import Links


class Buttons(BasePage):
    PAGE_URL = Links.BUTTONS

    DOUBLE_CLICK_BUTTON = ("xpath", "//button[@id='doubleClickBtn']")
    RIGHT_CLICK_BUTTON = ("css selector", "button[id='rightClickBtn']")
    CLICK_ME_BUTTON = ("xpath", "//button[text()='Click Me']")

    SUCCESS_DOUBLE_LOCATOR = ("xpath", "//p[@id='doubleClickMessage']")
    SUCCESS_RIGHT_LOCATOR = ("css selector", "p[id='rightClickMessage']")
    SUCCESS_CLICK_ME_LOCATOR = ("css selector", "p[id='dynamicClickMessage']")

    SUCCESS_DOUBLE_TEXT = "You have done a double click"
    SUCCESS_RIGHT_TEXT = "You have done a right click"
    SUCCESS_CLICK_ME_TEXT = "You have done a dynamic click"

    @allure.step("Perform double click on the button")
    def double_click(self):
        self.action_double_click(self.element_is_clickable(self.DOUBLE_CLICK_BUTTON))

    @allure.step("Perform right click on the button")
    def right_click(self):
        self.action_right_click(self.element_is_clickable(self.RIGHT_CLICK_BUTTON))

    @allure.step("Click on the button")
    def click(self):
        self.element_is_clickable(self.CLICK_ME_BUTTON).click()

    @allure.step("Check if double click message is displayed")
    def check_double_click(self):
        self.check_element_text(self.SUCCESS_DOUBLE_LOCATOR, self.SUCCESS_DOUBLE_TEXT)

    @allure.step("Check if right click message is displayed")
    def check_right_click(self):
        self.check_element_text(self.SUCCESS_RIGHT_LOCATOR, self.SUCCESS_RIGHT_TEXT)

    @allure.step("Check if a click message is displayed")
    def check_a_click(self):
        self.check_element_text(self.SUCCESS_CLICK_ME_LOCATOR, self.SUCCESS_CLICK_ME_TEXT)