import allure
from base.base_page import BasePage
from config.urls import Urls


class SelectMenu(BasePage):
    PAGE_URL = Urls.SELECT_MENU

    SELECT_VALUE = ("xpath", '//div[@id="withOptGroup"]')
    SELECT_ONE = ("xpath", '//div[@id="selectOne"]')
    SELECT_VALUE_OPTIONS = ("xpath", '//div[@tabindex="-1"]')
    SELECT_OLD_STYLE_MENU = ("xpath", '//select[@id="oldSelectMenu"]')
    SELECT_OLD_STYLE_MENU_OPTIONS = ("xpath", '//select[@id="oldSelectMenu"] //option[@value]')
    MULTISELECT_DROPDOWN = ("xpath", '//p/b[text()="Multiselect drop down"]/following::div[contains(@class, "css-yk16xz-control")][1]')
    STANDARD_MULTISELECT_DROPDOWN = ("xpath", '//select[@id="cars"]')


    @allure.step("Select option in Value dropdown")
    def select_value_option(self):
        self.select_dropdown_option_from_div(self.SELECT_VALUE,self.SELECT_VALUE_OPTIONS)

    @allure.step("Select option in One dropdown")
    def select_one_option(self):
        self.select_dropdown_option_from_div(self.SELECT_ONE,self.SELECT_VALUE_OPTIONS)

    @allure.step("Select option in Old Style Menu dropdown")
    def select_old_style_menu_option(self):
        self.select_random_option_from_select(self.SELECT_OLD_STYLE_MENU)

    @allure.step("Select random option in multiselect dropdown")
    def select_multiselect_dropdown(self):
        self.select_multiple_options_from_div(self.MULTISELECT_DROPDOWN,self.SELECT_VALUE_OPTIONS)

    @allure.step("Select random option in standard multiselect dropdown")
    def select_standard_multiselect_dropdown(self):
        self.select_multiple_options_from_select(self.STANDARD_MULTISELECT_DROPDOWN)