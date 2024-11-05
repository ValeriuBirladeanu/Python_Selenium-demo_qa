import allure
from base.base_page import BasePage
from config.urls import Urls


class Accordian(BasePage):
    PAGE_URL = Urls.ACCORDIAN

    CARD_HEADER = ("xpath", "//div[@class='card']")
    CARD_PARAGRAPH = ("xpath", ".//div[@class='collapse show']//div[@class='card-body']")

    @allure.step("Select another accordian")
    def select_accordian(self):
        accordian = self.elements_are_visible(self.CARD_HEADER)
        self.initially_opened_accordion = accordian[0]
        self.initially_opened_accordion_paragraph = self.element_is_visible(self.CARD_PARAGRAPH).text
        self.element_is_clickable(self.initially_opened_accordion).click()
        accordian_to_open = accordian[1:]
        self.new_accordion = self.get_random_element(accordian_to_open)
        self.scroll_to(self.new_accordion)
        self.element_is_clickable(self.new_accordion).click()
        self.new_accordion_paragraph = self.element_is_visible(self.CARD_PARAGRAPH).text

    @allure.step("Check opened new accordian(")
    def check_open_new_accordian(self):
        self.verify_change_text(self.initially_opened_accordion.text, self.new_accordion.text)
        self.verify_change_text(self.initially_opened_accordion_paragraph, self.new_accordion_paragraph)