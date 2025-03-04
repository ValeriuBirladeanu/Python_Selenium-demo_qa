import allure
from base.base_page import BasePage
from config.urls import Urls


class ToolTips(BasePage):
    PAGE_URL = Urls.TOOL_TIPS

    BUTTON_HOVE_ME_TO_SEE = ("xpath", '//button[@id="toolTipButton"]')
    HOVER_BUTTON_HOVE_ME_TO_SEE = ("xpath", '//div[@class="tooltip-inner" and text()="You hovered over the Button"]')
    INPUT_HOVE_ME_TO_SEE = ("xpath", '//div[@id="texFieldToolTopContainer"]')
    HOVER_INPUT_HOVE_ME_TO_SEE = ("xpath", '//div[@class="tooltip-inner" and text()="You hovered over the text field"]')
    TEXT_LINK_Contrary = ("xpath", '//a[@href="javascript:void(0)" and text() = "Contrary"]')
    HOVER_TEXT_LINK_Contrary = ("xpath", '//div[@class="tooltip-inner" and text()="You hovered over the Contrary"]')
    TEXT_LINK_1_10_32 = ("xpath", '//a[@href="javascript:void(0)" and text() = "1.10.32"]')
    HOVER_TEXT_LINK_1_10_32 = ("xpath", '//div[@class="tooltip-inner" and text()="You hovered over the 1.10.32"]')

    @allure.step("Check tooltip - button")
    def check_tooltip_button(self):
        actual_text = self.get_text_from_tooltips(self.BUTTON_HOVE_ME_TO_SEE, self.HOVER_BUTTON_HOVE_ME_TO_SEE)
        expected_text = "You hovered over the Button"
        self.check_if_text_matches(actual_text, expected_text)

    @allure.step("Check tooltip - input")
    def check_tooltip_input(self):
        actual_text = self.get_text_from_tooltips(self.INPUT_HOVE_ME_TO_SEE, self.HOVER_INPUT_HOVE_ME_TO_SEE)
        expected_text = "You hovered over the text field"
        self.check_if_text_matches(actual_text, expected_text)

    @allure.step("Check tooltip - text: Contrary ")
    def check_tooltip_text_contrary(self):
        actual_text = self.get_text_from_tooltips(self.TEXT_LINK_Contrary, self.HOVER_TEXT_LINK_Contrary)
        expected_text = "You hovered over the Contrary"
        self.check_if_text_matches(actual_text, expected_text)

    @allure.step("Check tooltip - text: 1_10_32")
    def check_tooltip_text_1_10_32(self):
        actual_text = self.get_text_from_tooltips(self.TEXT_LINK_1_10_32, self.HOVER_TEXT_LINK_1_10_32)
        expected_text = "You hovered over the 1.10.32"
        self.check_if_text_matches(actual_text, expected_text)