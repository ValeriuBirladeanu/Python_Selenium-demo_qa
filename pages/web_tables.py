import allure
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
    ALL_CELLS_TABLE_ELEMENTS = ("xpath", "//div[@class='rt-td']")
    All_ROWS_TABLE_ELEMENTS = ("xpath", "//div[@role='row']")
    SEARCH_INPUT = ("xpath", "//input[@id='searchBox']")
    ALL_EDIT_BUTTONS = ("xpath", "//span[@title='Edit']")

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
        self.check_element_value(self.DEPARTMENT_INPUT, self.department)

    @allure.step("Verify text in table entries")
    def verify_text_in_table_entries(self):
        self.check_text_in_multiple_elements(self.ALL_CELLS_TABLE_ELEMENTS, self.first_name)
        self.check_text_in_multiple_elements(self.ALL_CELLS_TABLE_ELEMENTS, self.last_name)
        self.check_text_in_multiple_elements(self.ALL_CELLS_TABLE_ELEMENTS, self.email)
        self.check_text_in_multiple_elements(self.ALL_CELLS_TABLE_ELEMENTS, self.age)
        self.check_text_in_multiple_elements(self.ALL_CELLS_TABLE_ELEMENTS, self.salary)
        self.check_text_in_multiple_elements(self.ALL_CELLS_TABLE_ELEMENTS, self.department)

    @allure.step('Select a random person and perform a search')
    def search_some_person(self):
        cells = self.elements_are_visible(self.ALL_CELLS_TABLE_ELEMENTS)
        cells = cells[1:]
        self.search_input = WebTables.get_random_text_element(cells).text
        search_input_element = self.element_is_clickable(self.SEARCH_INPUT)
        search_input_element.clear()
        search_input_element.send_keys(self.search_input)
        return self.search_input

    @allure.step('Verify the search result contains the searched person')
    def check_search_person(self):
        self.check_text_in_multiple_elements(self.ALL_CELLS_TABLE_ELEMENTS, self.search_input)
        return self.search_input

    @allure.step('Select a random row from the table')
    def select_random_row(self):
        edit_buttons = self.elements_are_visible(self.ALL_EDIT_BUTTONS)
        random_edit_button = WebTables.get_random_element(edit_buttons)
        self.element_is_clickable(random_edit_button).click()
        return random_edit_button

    @allure.step('Select a random field to edit')
    def select_random_field(self):
        fields = [
            {'type': 'first_name', 'locator': self.FIRST_NAME_INPUT},
            {'type': 'last_name', 'locator': self.LAST_NAME_INPUT},
            {'type': 'age', 'locator': self.AGE_INPUT},
            {'type': 'email', 'locator': self.EMAIL_INPUT},
            {'type': 'salary', 'locator': self.SALARY_INPUT},
            {'type': 'department', 'locator': self.DEPARTMENT_INPUT},
        ]
        return WebTables.get_random_element(fields)

    @allure.step('Generate a new value for the field of type {field_type}')
    def generate_new_value(self, field_type):
        if field_type == 'first_name':
            return self.data_generator.generate_first_name()
        elif field_type == 'last_name':
            return self.data_generator.generate_last_name()
        elif field_type == 'age':
            return self.data_generator.generate_age()
        elif field_type == 'email':
            return self.data_generator.generate_email()
        elif field_type == 'salary':
            return self.data_generator.generate_salary()
        elif field_type == 'department':
            return self.data_generator.generate_department()
        else:
            raise ValueError(f"Unknown field type: {field_type}")

    @allure.step('Modify the field with the new value')
    def modify_field(self, input_element, new_value):
        input_element.clear()
        input_element.send_keys(new_value)
        self.element_is_clickable(self.SUBMIT_BUTTON).click()

    @allure.step('Verify the new text in the table')
    def verify_text_in_table(self, expected_text):
        self.check_text_in_multiple_elements(self.ALL_CELLS_TABLE_ELEMENTS, expected_text)

    @allure.step('Edit some person details randomly')
    def edit_some_person(self):
        self.select_random_row()
        field_to_edit = self.select_random_field()
        field_input = self.element_is_visible(field_to_edit['locator'])
        new_value = self.generate_new_value(field_to_edit['type'])
        self.modify_field(field_input, new_value)
        self.verify_text_in_table(new_value)