import random
import allure
from selenium.webdriver import Keys
from base.base_page import BasePage
from config.urls import Urls


class AutoComplete(BasePage):
    PAGE_URL = Urls.AUTO_COMPLETE

    MULTIPLE_NAMES_INPUT = ("css selector", "[id='autoCompleteMultipleInput']")
    MULTIPLE_NAMES_VALUE = ("css selector", "div[class*='auto-complete__value-container--is-multi']")
    MULTIPLE_DROP_DOWN = ("css selector", "div[class*='auto-complete__menu-list--is-multi css-11unzgr']")
    SINGLE_NAME_INPUT = ("css selector", "[id='autoCompleteSingleInput']")
    SINGLE_NAME_VALUE = ("css selector", "[class*='auto-complete__value-container auto-complete__value-container--has']")
    SINGLE_DROP_DOWN = ("css selector", "div[class='auto-complete__menu-list css-11unzgr']")

    @allure.step("Select multiple names input")
    def choose_multiple_names_input(self):
        self.multimple_names = self.element_is_clickable(self.MULTIPLE_NAMES_INPUT)
        self.multimple_names.click()
        self.num_values_to_select = random.randint(2, 5)
        self.selected_values = []
        for _ in range(self.num_values_to_select):
            random_letter = random.choice('agent')  # Choose a random letter in each iteration
            self.multimple_names.send_keys(random_letter)
            self.element_is_visible(self.MULTIPLE_DROP_DOWN)
            self.multimple_names.send_keys(Keys.TAB)
            input_value_element = self.element_is_presence(self.MULTIPLE_NAMES_VALUE)
            input_value = input_value_element.get_attribute('innerText').strip().replace("\n", " ")
            selected_name = input_value.split()[-1]
            self.selected_values.append(selected_name)

    @allure.step("Check selected multiple names input")
    def check_completed_multiple_names_input(self):
        assert self.selected_values, "No value was selected."
        assert len(self.selected_values) == self.num_values_to_select, \
            (f"Number of values selected is not correct. Expected {self.num_values_to_select}, "
             f"but selected {len(self.selected_values)}.")

    @allure.step("Select single name input")
    def choose_single_name_input(self):
        self.single_name = self.element_is_clickable(self.SINGLE_NAME_INPUT)
        self.single_name.click()
        random_letter = random.choice('agent')  # Choose a random letter
        self.single_name.send_keys(random_letter)
        self.element_is_visible(self.SINGLE_DROP_DOWN)
        self.single_name.send_keys(Keys.TAB)
        input_value_element = self.element_is_presence(self.SINGLE_NAME_VALUE)
        input_value = input_value_element.get_attribute('innerText')
        self.selected_value = [input_value]

    @allure.step("Check selected single name input")
    def check_completed_single_name_input(self):
        assert self.selected_value, "No value was selected."
        assert len(self.selected_value) == 1, (f"Number of values selected is not correct. "
                                               f"Expected 1, but selected {len(self.selected_value)}.")