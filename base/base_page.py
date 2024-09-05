import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        with allure.step(f"Open {self.PAGE_URL} page"):
            self.driver.get(self.PAGE_URL)  # Opening the web page

    def is_opened(self):
        with allure.step(f"Page {self.PAGE_URL} is opened"):
            self.wait.until(EC.url_to_be(self.PAGE_URL))  # Checking if the web page has been opened

    def element_is_visible(self, locator):
        with allure.step(f"Check visibility of element located by {locator}"):
            return self.wait.until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator):
        with allure.step(f"Check visibility of elements located by {locator}"):
            return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def element_is_clickable(self, locator):
        with allure.step(f"Check if element located by {locator} is clickable"):
            return self.wait.until(EC.element_to_be_clickable(locator))

    def element_is_selected(self, locator):
        with allure.step(f"Check if element located by {locator} is selected"):
            return self.wait.until(EC.element_located_to_be_selected(locator))

    def element_is_presence(self, locator):
        with allure.step(f"Check presence of element located by {locator}"):
            return self.wait.until(EC.presence_of_element_located(locator))

    def elements_are_presence(self, locator):
        with allure.step(f"Check presence of elements located by {locator}"):
            return self.wait.until(EC.presence_of_all_elements_located(locator))

    def wait_for_element_value(self, locator, value):
        with allure.step(f"Wait for element located by {locator} to have value '{value}'"):
            element = self.wait.until(EC.presence_of_element_located(locator))
            actual_value = element.get_attribute('value')
            assert value.lower() == actual_value.lower(), f"Expected value '{value}' but got '{actual_value}'"
            return element

    def wait_for_element_text(self, locator, expected_text, slicing=None):
        with allure.step(f"Wait for element located by {locator} to contain text '{expected_text}'"):
            element = self.wait.until(EC.presence_of_element_located(locator))
            actual_text = slicing(element.text) if slicing else element.text
            assert expected_text.lower() in actual_text.lower(), f"Expected text '{expected_text}' in '{actual_text}' (full text: '{element.text}')"
            return element

    def scroll_to(self, target):
        if isinstance(target, tuple):  # Check if target is a locator
            element = self.driver.find_element(*target)
        else:  # Assumes target is a web element
            element = target
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def make_screenshot(self):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name="Screenshot",
            attachment_type=AttachmentType.PNG
        )