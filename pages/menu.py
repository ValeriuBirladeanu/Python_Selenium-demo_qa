import allure
from base.base_page import BasePage
from config.urls import Urls


class Menu(BasePage):
    PAGE_URL = Urls.MENU

    MENU_ITEM_LIST = ("css selector", 'ul[id="nav"] li a')

    @allure.step("Receiving the names of all menus")
    def receiving_names_of_all_menus(self):
        menu_item_list = self.elements_are_presence(self.MENU_ITEM_LIST)
        self.data_txt_list = []
        for item in menu_item_list:
            self.action_move_to_element(item)
            self.data_txt_list.append(item.text)

    @allure.step("Check menu names")
    def check_menu_names(self):
        expected_menu_items = ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1', 'Sub Sub Item 2', 'Main Item 3']
        assert self.data_txt_list == expected_menu_items, f"Expected menu items: {expected_menu_items} but got: {self.data_txt_list}"