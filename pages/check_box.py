import random
import allure
from base.base_page import BasePage
from config.links import Links


class CheckBox(BasePage):
    PAGE_URL = Links.CHECK_BOX

    EXPAND_ALL_BUTTON = ("xpath", "//button[@title='Expand all']")
    ITEM_LIST = ("xpath", "//span[@class='rct-title']")
    CHECKED_ITEMS = ("css selector", "svg.rct-icon.rct-icon-check")
    TITLE_ITEM = ("xpath", ".//ancestor::span[@class='rct-text']")
    OUTPUT_RESULT = ("xpath", "//span[@class='text-success']")

    @allure.step("Click Expand All button")
    def click_expand_all(self):
        self.element_is_clickable(self.EXPAND_ALL_BUTTON).click()

    @allure.step("Verify checkboxes are visible and clickable")
    def verify_checkboxes_visible_and_clickable(self):
        checkboxes = self.elements_are_visible(self.ITEM_LIST)
        for checkbox in checkboxes:
            assert checkbox.is_displayed(), f"Checkbox {checkbox.text} is not visible."
            assert checkbox.is_enabled(), f"Checkbox {checkbox.text} is not clickable."

    @allure.step("Click random checkbox")
    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.ITEM_LIST)
        count = 17
        while count != 0:
            item = item_list[random.randint(0, len(item_list) - 1)]
            self.scroll_to(item)
            item.click()
            count -= 1

    @allure.step("Get checked checkboxes")
    def get_checked_checkboxes(self):
        checked_list = self.elements_are_visible(self.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(*self.TITLE_ITEM)
            data.append(title_item.text)
        formatted_data  = str(data).replace(" ", "").replace("doc", "").replace(".", "").lower()
        return formatted_data

    @allure.step("Get output results")
    def get_output_results(self):
        result_list = self.elements_are_visible(self.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        formatted_data  = str(data).replace(" ", "").lower()
        return formatted_data

    @allure.step("Verify checkbox selections are reflected in output results")
    def verify_checkbox_selections(self):
        input_result = self.get_checked_checkboxes()
        output_result = self.get_output_results()
        assert input_result == output_result, f"Mismatch between input and output results: {input_result} != {output_result}"