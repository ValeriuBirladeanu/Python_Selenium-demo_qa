import allure
from base.base_page import BasePage
from config.urls import Urls
from data.data_generator import TestDataGenerator

class TextBox(BasePage):
    PAGE_URL = Urls.TEXT_BOX

    FULL_NAME_FIELD = ("xpath", "//input[@id='userName']")
    EMAIL_FIELD = ("xpath", "//input[@id='userEmail']")
    CURRENT_ADDRESS_FIELD = ("xpath", "//textarea[@id='currentAddress']")
    PERMANENT_ADDRESS_FIELD = ("xpath", "//textarea[@id='permanentAddress']")
    SUBMIT_BUTTON = ("xpath", "//button[@id='submit']")

    OUTPUT_FULL_NAME = ("xpath", "//p[@id='name']")
    OUTPUT_EMAIL = ("xpath", "//p[@id='email']")
    OUTPUT_CURRENT_ADDRESS = ("xpath", "//p[@id='currentAddress']")
    OUTPUT_PERMANENT_ADDRESS = ("xpath", "//p[@id='permanentAddress']")

    def __init__(self, driver):
        super().__init__(driver)
        self.data_generator = TestDataGenerator()

    @allure.step("Enter full name")
    def enter_full_name(self):
        self.full_name = self.data_generator.generate_full_name()
        self.element_is_clickable(self.FULL_NAME_FIELD).send_keys(self.full_name)

    @allure.step("Enter email")
    def enter_email(self):
        self.email = self.data_generator.generate_email()
        self.element_is_clickable(self.EMAIL_FIELD).send_keys(self.email)

    @allure.step("Enter current address")
    def enter_current_address(self):
        self.current_address = self.data_generator.generate_current_address()
        self.element_is_clickable(self.CURRENT_ADDRESS_FIELD).send_keys(self.current_address)

    @allure.step("Enter permanent address")
    def enter_permanent_address(self):
        self.permanent_address = self.data_generator.generate_permanent_address()
        self.element_is_clickable(self.PERMANENT_ADDRESS_FIELD).send_keys(self.permanent_address)

    @allure.step("Click submit button")
    def click_submit(self):
        self.scroll_to(self.SUBMIT_BUTTON)
        self.element_is_clickable(self.SUBMIT_BUTTON).click()

    @allure.step("Verify saved full name")
    def is_saved_full_name(self):
        self.check_element_value(self.FULL_NAME_FIELD, self.full_name)
        self.check_element_text(self.OUTPUT_FULL_NAME, self.full_name, lambda slicing: slicing.split(":")[1])

    @allure.step("Verify saved email")
    def is_saved_email(self):
        self.check_element_value(self.EMAIL_FIELD, self.email),
        self.check_element_text(self.OUTPUT_EMAIL, self.email, lambda slicing: slicing.split(":")[1])

    @allure.step("Verify saved current address")
    def is_saved_current_address(self):
        self.check_element_value(self.CURRENT_ADDRESS_FIELD, self.current_address)
        self.check_element_text(self.OUTPUT_CURRENT_ADDRESS, self.current_address, lambda slicing: slicing.split(":")[1])

    @allure.step("Verify saved permanent address")
    def is_saved_permanent_address(self):
        self.check_element_value(self.PERMANENT_ADDRESS_FIELD, self.permanent_address)
        self.check_element_text(self.OUTPUT_PERMANENT_ADDRESS, self.permanent_address, lambda slicing: slicing.split(":")[1])