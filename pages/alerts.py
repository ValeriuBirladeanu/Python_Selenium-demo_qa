import allure
import requests
from base.base_page import BasePage
from config.urls import Urls
from data.data_generator import TestDataGenerator


class Alerts(BasePage):
    PAGE_URL = Urls.ALERTS

    ALERT_BUTTON = ("xpath", "//button[@id='alertButton']")
    FIVE_SECOND_ALERT_BUTTON = ("xpath", "//button[@id='timerAlertButton']")
    CONFIRM_ALERT_BUTTON = ("xpath", "//button[@id='confirmButton']")
    CONFIRM_RESULT = ("xpath", "//span[@id='confirmResult']")
    INPUT_ALERT_BUTTON = ("xpath", "//button[@id='promtButton']")
    INPUT_RESULT = ("xpath", "//span[@id='promptResult']")

    def __init__(self, driver):
        super().__init__(driver)
        self.data_generator = TestDataGenerator()


    """ALERT_BUTTON"""
    @allure.step("Click on alert_button")
    def click_alert_button(self):
        self.element_is_clickable(self.ALERT_BUTTON).click()

    @allure.step("Check if alert_button alert opened")
    def check_opened_alert(self):
        self.alert_is_present()
        self.switch_to_alert()
        expected_text = "You clicked a button"
        self.check_alert_text(self.alert.text, expected_text)

    @allure.step("Accept alert")
    def accept_alert(self):
        self.alert.accept()

    @allure.step("Dismiss alert")
    def dismiss_alert(self):
        self.alert.dismiss()

    """FIVE_SECOND_ALERT_BUTTON"""
    @allure.step("Click on five_second_alert_button")
    def click_five_seconds_alert_button(self):
        self.element_is_clickable(self.FIVE_SECOND_ALERT_BUTTON).click()

    @allure.step("Check if five_second_alert_button alert opened after 5 seconds")
    def check_opened_five_seconds_alert(self):
        self.alert_is_present()
        self.switch_to_alert()
        expected_text = "This alert appeared after 5 seconds"
        self.check_alert_text(self.alert.text, expected_text)

    """CONFIRM_ALERT_BUTTON"""
    @allure.step("Click on confirm_alert_button")
    def click_confirm_alert_button(self):
        self.element_is_clickable(self.CONFIRM_ALERT_BUTTON).click()

    @allure.step("Check if confirm_alert_button alert opened")
    def check_opened_confirm_alert(self):
        self.alert_is_present()
        self.switch_to_alert()
        expected_text = "Do you confirm action?"
        self.check_alert_text(self.alert.text, expected_text)

    @allure.step("Check confirmed text in alert result")
    def check_confirmed_text(self, expected_text):
        self.check_element_text(self.CONFIRM_RESULT, expected_text)

    """INPUT_ALERT_BUTTON"""
    @allure.step("Click on input_alert_button")
    def click_input_alert_button(self):
        self.element_is_clickable(self.INPUT_ALERT_BUTTON).click()

    @allure.step("Check if input_alert_button alert opened")
    def check_opened_input_alert(self):
        self.alert_is_present()
        self.switch_to_alert()
        expected_text = "Please enter your name"
        self.check_alert_text(self.alert.text, expected_text)

    @allure.step("Enter text in input_alert_button alert")
    def enter_text_in_input_alert_button(self):
        self.text = self.data_generator.generate_full_name()
        self.enter_text_to_alert(self.text)

    @allure.step("Check confirmed text in input_alert_button result")
    def check_opened_confirmed_text(self):
        self.check_element_text(self.INPUT_RESULT, self.text, lambda slicing: " ".join(slicing.split(" ")[-2:]))