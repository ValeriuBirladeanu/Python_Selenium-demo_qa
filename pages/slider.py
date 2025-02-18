import random
import allure
from base.base_page import BasePage
from config.urls import Urls


class Slider(BasePage):
    PAGE_URL = Urls.SLIDER

    INPUT_SLIDER = ("xpath", '//input[@class="range-slider range-slider--primary"]')
    VALUE_SLIDER = ("xpath", '//input[@id="sliderValue"]')

    @allure.step("Change slider value")
    def change_slider_value(self):
        self.value_before = self.element_is_visible(self.VALUE_SLIDER).get_attribute('value')
        print(self.value_before)
        input_slider = self.element_is_visible(self.INPUT_SLIDER)
        self.action_drag_and_drop_by_offset(input_slider, random.randint(1,100), 0)
        self.value_after = self.element_is_presence(self.VALUE_SLIDER).get_attribute('value')
        print(self.value_after)

    @allure.step("Check the value change after applying the slider")
    def check_slider_value_change(self):
        self.verify_value_change(self.value_before, self.value_after)