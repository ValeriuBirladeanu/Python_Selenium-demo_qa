import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from data.data_generator import TestDataGenerator

class TextBox(BasePage):
    PAGE_URL = Links.TEXT_BOX

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
        self.wait.until(EC.element_to_be_clickable(self.FULL_NAME_FIELD)).send_keys(self.full_name)

    @allure.step("Enter email")
    def enter_email(self):
        self.email = self.data_generator.generate_email()
        self.wait.until(EC.element_to_be_clickable(self.EMAIL_FIELD)).send_keys(self.email)

    @allure.step("Enter current address")
    def enter_current_address(self):
        self.current_address = self.data_generator.generate_current_address()
        self.wait.until(EC.element_to_be_clickable(self.CURRENT_ADDRESS_FIELD)).send_keys(self.current_address)

    @allure.step("Enter permanent address")
    def enter_permanent_address(self):
        self.permanent_address = self.data_generator.generate_permanent_address()
        self.wait.until(EC.element_to_be_clickable(self.PERMANENT_ADDRESS_FIELD)).send_keys(self.permanent_address)

    @allure.step("Click submit button")
    def click_submit(self):
        self.scroll_to_element(self.SUBMIT_BUTTON)
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    @allure.step("Verify saved full name")
    def is_saved_full_name(self):
        assert self.wait.until(EC.text_to_be_present_in_element_value(self.FULL_NAME_FIELD, self.full_name)), "Full name was not saved correctly in the input field"
        saved_full_name = self.wait.until(EC.presence_of_element_located(self.OUTPUT_FULL_NAME)).text.split(":")[1].strip()
        assert saved_full_name == self.full_name, f"Expected '{self.full_name}', but got '{saved_full_name}'"

    @allure.step("Verify saved email")
    def is_saved_email(self):
        assert self.wait.until(EC.text_to_be_present_in_element_value(self.EMAIL_FIELD, self.email)), "Email was not saved correctly in the input field"
        saved_email = self.wait.until(EC.presence_of_element_located(self.OUTPUT_EMAIL)).text.split(":")[1].strip()
        assert saved_email == self.email, f"Expected '{self.email}', but got '{saved_email}'"

    @allure.step("Verify saved current address")
    def is_saved_current_address(self):
        assert self.wait.until(EC.text_to_be_present_in_element_value(self.CURRENT_ADDRESS_FIELD, self.current_address)), "Current address was not saved correctly in the input field"
        saved_current_address = self.wait.until(EC.presence_of_element_located(self.OUTPUT_CURRENT_ADDRESS)).text.split(":")[1].strip()
        assert saved_current_address == self.current_address, f"Expected '{self.current_address}', but got '{saved_current_address}'"

    @allure.step("Verify saved permanent address")
    def is_saved_permanent_address(self):
        assert self.wait.until(EC.text_to_be_present_in_element_value(self.PERMANENT_ADDRESS_FIELD, self.permanent_address)), "Permanent address was not saved correctly in the input field"
        saved_permanent_address = self.wait.until(EC.presence_of_element_located(self.OUTPUT_PERMANENT_ADDRESS)).text.split(":")[1].strip()
        assert saved_permanent_address == self.permanent_address, f"Expected '{self.permanent_address}', but got '{saved_permanent_address}'"
