from random import choice
import allure
from base.base_page import BasePage
from config.links import Links


class RadioButton(BasePage):
    PAGE_URL = Links.RADIO_BUTTON

    RADIO_BUTTON_ACTION = {
        "yes": ("xpath", "//label[@for='yesRadio']"),
        "impressive": ("xpath", "//label[@for='impressiveRadio']")
    }
    RADIO_BUTTON_CHECK = {
        "yes": ("xpath", "//input[@id='yesRadio']"),
        "impressive": ("xpath", "//input[@id='impressiveRadio']")
    }
    NO_RADIO_BUTTON_CHECK = ("xpath", "//input[@id='noRadio']")
    OUTPUT_RESULT = ("xpath", "//span[@class='text-success']")

    @allure.step("Click a random radio button and verify selection")
    def click_random_radio_button_and_verify(self):
        first_button = choice(["yes", "impressive"])
        second_button = "impressive" if first_button == "yes" else "yes"

        self.click_on_radio_button(first_button)
        self.check_if_radio_button_is_selected(first_button)
        self.is_present_confirmation_text(first_button)

        self.click_on_radio_button(second_button)
        self.check_if_radio_button_is_selected(second_button)
        self.is_present_confirmation_text(second_button)

        self.check_if_radio_button_is_not_selected(first_button)

    @allure.step("Click on a radio button")
    def click_on_radio_button(self, button_type):
        locator = self.RADIO_BUTTON_ACTION[button_type]
        self.element_is_clickable(locator).click()

    @allure.step("Check if the radio button is selected")
    def check_if_radio_button_is_selected(self, button_type):
        locator = self.RADIO_BUTTON_CHECK[button_type]
        element = self.element_is_presence(locator)
        is_selected = element.is_selected()
        assert is_selected, f"'{button_type}' radio button should be selected"
        return is_selected

    @allure.step("Check if the radio button is not selected")
    def check_if_radio_button_is_not_selected(self, button_type):
        locator = self.RADIO_BUTTON_CHECK[button_type]
        element = self.element_is_presence(locator)
        is_selected = element.is_selected()
        assert not is_selected, f"'{button_type}' radio button should not be selected"
        return is_selected

    @allure.step("Verify presence text for a radio button")
    def is_present_confirmation_text(self, button_type):
        expected_text = button_type
        self.wait_for_element_text(self.OUTPUT_RESULT, expected_text)

    @allure.step("Check if the 'No' radio button is disabled")
    def check_if_no_radio_button_is_disabled(self):
        element = self.element_is_presence(self.NO_RADIO_BUTTON_CHECK)
        is_disabled = element.get_attribute("disabled") is not None
        assert is_disabled, "'No' radio button should be disabled"
        return is_disabled