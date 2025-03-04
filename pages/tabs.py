import allure
from base.base_page import BasePage
from config.urls import Urls


class Tabs(BasePage):
    PAGE_URL = Urls.TABS

    TAB_HEADER_SELECTED = ("xpath", "//a[@class='nav-item nav-link active']")
    TAB_HEADER_ANOTHER = ("xpath", "//a[@class='nav-item nav-link']")
    TAB_PARAGRAPH = ("xpath", "//div[@class='fade tab-pane active show'] //p[@class='mt-3']")

    @allure.step("Select another tab")
    def select_another_tab(self):
        self.initially_opened_tab = self.element_is_visible(self.TAB_HEADER_SELECTED)
        self.initially_opened_tab_paragraph = self.element_is_visible(self.TAB_PARAGRAPH).text
        tabs = self.elements_are_visible(self.TAB_HEADER_ANOTHER)
        self.new_tab = self.get_random_element(tabs)
        self.element_is_clickable(self.new_tab).click()
        self.new_tab_paragraph = self.element_is_visible(self.TAB_PARAGRAPH).text

    @allure.step("Check opened new tab(")
    def check_open_new_tab(self):
        self.verify_change_text(self.initially_opened_tab.text, self.new_tab.text)
        self.verify_change_text(self.initially_opened_tab_paragraph, self.new_tab_paragraph)