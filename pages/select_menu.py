import allure
from base.base_page import BasePage
from config.urls import Urls


class SelectMenu(BasePage):
    PAGE_URL = Urls.SELECT_MENU

    SELECT_VALUE = ("xpath", '//div[@id="withOptGroup"]')
    SELECT_ONE = ("xpath", '//div[@id="selectOne"]')
    SELECT_VALUE_ONE_OPTIONS = ("xpath", '//div[@tabindex="-1"]')
    SELECT_OLD_STYLE_MENU = ("xpath", '//select[@id="oldSelectMenu"]')
    MULTISELECT_DROPDOWN = ("xpath", '//p/b[text()="Multiselect drop down"]/following::div[contains(@class, "css-yk16xz-control")][1]')
    STANDARD_MULTISELECT_DROPDOWN = ("xpath", '//select[@id="cars"]')

    SELECT_VALUE_SELECTED  = ("xpath", '//div[@id="withOptGroup"] //div[@class=" css-1uccc91-singleValue"]')
    SELECT_ONE_SELECTED = ("xpath", '//div[@id="selectOne"] //div[@class=" css-1uccc91-singleValue"]')
    MULTISELECT_DROPDOWN_SELECTED = ("xpath", '//div[@class="css-12jo7m5"]')

    @allure.step("Select option in Value dropdown")
    def select_value_dropdown(self):
        self.selected_value  = self.select_dropdown_option_from_div(self.SELECT_VALUE,self.SELECT_VALUE_ONE_OPTIONS)

    @allure.step("Select option in One dropdown")
    def select_one_dropdown(self):
        self.selected_one = self.select_dropdown_option_from_div(self.SELECT_ONE,self.SELECT_VALUE_ONE_OPTIONS)

    @allure.step("Select option in Old Style Menu dropdown")
    def select_old_style_menu_dropdown(self):
        self.selected_old_style = self.select_option_from_select(self.SELECT_OLD_STYLE_MENU)

    @allure.step("Select option in Multiselect dropdown")
    def select_multiselect_dropdown(self):
        self.selected_values_multiselect = self.select_multiple_options_from_div(self.MULTISELECT_DROPDOWN,self.SELECT_VALUE_ONE_OPTIONS)

    @allure.step("Select option in Standard Multiselect dropdown")
    def select_standard_multiselect_dropdown(self):
        self.selected_values_standard_multiselect = self.select_multiple_options_from_select(self.STANDARD_MULTISELECT_DROPDOWN)


    @allure.step("Check select option in Value dropdown")
    def check_select_value_option_dropdown(self):
        actual_value = self.element_is_visible(self.SELECT_VALUE_SELECTED).text
        self.check_if_text_matches(actual_value, self.selected_value)

    @allure.step("Check select option in One dropdown")
    def check_select_one_option_dropdown(self):
        actual_value = self.element_is_visible(self.SELECT_ONE_SELECTED).text
        self.check_if_text_matches(actual_value, self.selected_one)

    @allure.step("Check select option in Old Style Menu dropdown")
    def check_select_old_style_menu_option_dropdown(self):
        actual_value = self.get_selected_option_text_from_select(self.SELECT_OLD_STYLE_MENU)
        self.check_if_text_matches(actual_value, self.selected_old_style)

    @allure.step("Check select option in Multiselect dropdown")
    def check_select_multiselect_option_dropdown(self):
        selected_elements  = self.elements_are_presence(self.MULTISELECT_DROPDOWN_SELECTED)
        actual_values = [element.text for element in selected_elements]
        self.check_if_text_matches(actual_values, self.selected_values_multiselect)

    @allure.step("Check select option in Standard Multiselect dropdown")
    def check_select_standard_multiselect_option_dropdown(self):
        selected_elements = self.elements_are_presence(self.STANDARD_MULTISELECT_DROPDOWN)
        actual_values = [element.text.strip() for element in selected_elements]
        actual_values = sorted([value.strip() for value in actual_values[0].split('\n')])
        expected_values = sorted(self.selected_values_standard_multiselect)
        self.check_if_text_matches(actual_values, expected_values)