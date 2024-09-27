import allure
from base.base_page import BasePage
from config.urls import Urls


class DynamicProperties(BasePage):
    PAGE_URL = Urls.DYNAMIC_PROPERTIES

    ENABLE_BUTTON = ("xpath", "//button[@id='enableAfter']")
    BUTTON_BEFORE_COLOR_CHANGE = ("xpath", "//button[@id='colorChange'][@class='mt-4 btn btn-primary']")
    BUTTON_AFTER_COLOR_CHANGE = ("xpath", "//button[@id='colorChange'][@class='mt-4 text-danger btn btn-primary']")
    VISIBLE_BUTTON = ("xpath", "//button[@id='visibleAfter']")

    @allure.step("Check enable button")
    def check_enable_button(self):
        enable_button = self.element_is_clickable(self.ENABLE_BUTTON)
        assert enable_button is not None, "The button did not become clickable within the expected time frame"

    @allure.step("Check button color change by class")
    def check_button_color_change(self):
        assert self.element_is_invisibility(self.BUTTON_BEFORE_COLOR_CHANGE), "Original button is still visible"
        assert self.element_is_visible(self.BUTTON_AFTER_COLOR_CHANGE), "New button with changed color is not visible"

    @allure.step("Check the appearance of the button")
    def check_appearance_button(self):
        visible_button = self.element_is_visible(self.VISIBLE_BUTTON)
        assert visible_button is not None, "The button is not visible"