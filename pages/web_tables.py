import time

import allure
from faker.generator import random

from base.base_page import BasePage
from config.links import Links
from data.data_generator import TestDataGenerator


class WebTables(BasePage):
    PAGE_URL = Links.WEB_TABLES

    ADD_BUTTON = ("xpath", "//button[@id='addNewRecordButton']")
    REGISTRATION_FORM  = ("xpath", "//form[@id='userForm']")
    FIRST_NAME_INPUT = ("xpath", "//input[@id='firstName']")
    LAST_NAME_INPUT = ("xpath", "//input[@id='lastName']")
    EMAIL_INPUT = ("xpath", "//input[@id='userEmail']")
    AGE_INPUT = ("xpath", "//input[@id='age']")
    SALARY_INPUT = ("xpath", "//input[@id='salary']")
    DEPARTMENT_INPUT = ("xpath", "//input[@id='department']")
    SUBMIT_BUTTON = ("xpath", "//button[@id='submit']")
    ALL_OUTPUT_CELLS_ELEMENTS = ("xpath", "//div[@class='rt-td']")
    SEARCH_INPUT = ("xpath", "//input[@id='searchBox']")
    ROW_TABLE = ("xpath", "//div[@role='row']")

    def __init__(self, driver):
        super().__init__(driver)
        self.data_generator = TestDataGenerator()

    @allure.step("Click add button")
    def click_add(self):
        self.element_is_clickable(self.ADD_BUTTON).click()

    @allure.step("Check modal window visibility")
    def check_open_modal_window(self):
        self.element_is_visible(self.REGISTRATION_FORM)

    @allure.step("Enter first name")
    def enter_first_name(self):
        self.first_name = self.data_generator.generate_first_name()[:25]
        self.element_is_clickable(self.FIRST_NAME_INPUT).send_keys(self.first_name)

    @allure.step("Enter last name")
    def enter_last_name(self):
        self.last_name = self.data_generator.generate_last_name()[:25]
        self.element_is_clickable(self.LAST_NAME_INPUT).send_keys(self.last_name)

    @allure.step("Enter email")
    def enter_email(self):
        self.email = self.data_generator.generate_email()
        self.element_is_clickable(self.EMAIL_INPUT).send_keys(self.email)

    @allure.step("Enter age")
    def enter_age(self):
        self.age = self.data_generator.generate_age()
        self.element_is_clickable(self.AGE_INPUT).send_keys(self.age)

    @allure.step("Enter salary")
    def enter_salary(self):
        self.salary = self.data_generator.generate_salary()
        self.element_is_clickable(self.SALARY_INPUT).send_keys(self.salary)

    @allure.step("Enter department")
    def enter_department(self):
        self.department = self.data_generator.generate_department()[:25]
        self.element_is_clickable(self.DEPARTMENT_INPUT).send_keys(self.department)

    @allure.step("Click submit button")
    def click_submit(self):
        self.element_is_clickable(self.SUBMIT_BUTTON).click()

    @allure.step("Check values in input fields")
    def check_values_in_input_fields(self):
        self.check_element_value(self.FIRST_NAME_INPUT, self.first_name)
        self.check_element_value(self.LAST_NAME_INPUT, self.last_name)
        self.check_element_value(self.EMAIL_INPUT, self.email)
        self.check_element_value(self.AGE_INPUT, self.age)
        self.check_element_value(self.SALARY_INPUT, self.salary)
        self.check_element_value(self.DEPARTMENT_INPUT, self.department, lambda slicing: slicing.strip())

    @allure.step("Verify text in table entries")
    def verify_text_in_table_entries(self):
        self.check_text_in_multiple_elements(self.ALL_OUTPUT_CELLS_ELEMENTS, self.first_name)
        self.check_text_in_multiple_elements(self.ALL_OUTPUT_CELLS_ELEMENTS, self.last_name)
        self.check_text_in_multiple_elements(self.ALL_OUTPUT_CELLS_ELEMENTS, self.email)
        self.check_text_in_multiple_elements(self.ALL_OUTPUT_CELLS_ELEMENTS, self.age)
        self.check_text_in_multiple_elements(self.ALL_OUTPUT_CELLS_ELEMENTS, self.salary)
        self.check_text_in_multiple_elements(self.ALL_OUTPUT_CELLS_ELEMENTS, self.department, lambda slicing: slicing.strip())

    @allure.step('Select a random person and perform a search')
    def search_some_person(self):
        cells = self.elements_are_visible(self.ALL_OUTPUT_CELLS_ELEMENTS)
        cells = cells[1:]
        self.search_input = self.get_random_element(cells).text
        search_input_element = self.element_is_clickable(self.SEARCH_INPUT)
        search_input_element.clear()
        search_input_element.send_keys(self.search_input)
        return self.search_input

    @allure.step('Verify the search result contains the searched person')
    def check_search_person(self):
        self.check_text_in_multiple_elements(self.ALL_OUTPUT_CELLS_ELEMENTS, self.search_input)
        return self.search_input