import random
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # Opening the web page
    def open(self):
        with allure.step(f"Open {self.PAGE_URL} page"):
            self.driver.get(self.PAGE_URL)

    # Checking if the web page has been opened
    def is_opened(self):
        with allure.step(f"Page {self.PAGE_URL} is opened"):
            self.wait.until(EC.url_to_be(self.PAGE_URL))

    # Checks if an element is visible on the page
    def element_is_visible(self, locator):
        with allure.step(f"Check visibility of element located by {locator}"):
            return self.wait.until(EC.visibility_of_element_located(locator))

    # Checks if multiple elements are visible on the page
    def elements_are_visible(self, locator):
        with allure.step(f"Check visibility of elements located by {locator}"):
            return self.wait.until(EC.visibility_of_all_elements_located(locator))

    # Checks if an element is clickable
    def element_is_clickable(self, locator):
        with allure.step(f"Check if element located by {locator} is clickable"):
            return self.wait.until(EC.element_to_be_clickable(locator))

    # Checks if an element is selected
    def element_is_selected(self, locator):
        with allure.step(f"Check if element located by {locator} is selected"):
            return self.wait.until(EC.element_located_to_be_selected(locator))

    # Checks if an element is present in the DOM
    def element_is_presence(self, locator):
        with allure.step(f"Check presence of element located by {locator}"):
            return self.wait.until(EC.presence_of_element_located(locator))

    # Checks if multiple elements are present in the DOM
    def elements_are_presence(self, locator):
        with allure.step(f"Check presence of elements located by {locator}"):
            return self.wait.until(EC.presence_of_all_elements_located(locator))

    # Checks if an element is invisibility in the DOM
    def element_is_invisibility(self, locator):
        with allure.step(f"Check invisibility of element located by {locator}"):
            return self.wait.until(EC.invisibility_of_element_located(locator))

    # Retrieve the color of the specified element
    def get_element_color(self, element):
        with allure.step(f"Retrieve the color of the specified element: {element}"):
            color = element.value_of_css_property('color')
            allure.attach(f"Element: {element}", name="Element")
            allure.attach(color, name="Element Color")
            return color

    # Checks if the value of an element changes to a new value
    def check_element_value(self, locator, new_value, slicing=None):
        with allure.step(f"Wait for element located by {locator} to change new value '{new_value}'"):
            element = self.wait.until(EC.visibility_of_element_located(locator))
            actual_value = element.get_attribute('value')
            actual_value = slicing(actual_value) if slicing else actual_value
            assert str(new_value).lower().strip() == str(actual_value).lower().strip(), f"Expected value '{new_value}' but got '{actual_value}'"
            return element

    def get_updated_value(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.get_attribute('value')

    # Checks if the text of an element contains the expected text
    def check_element_text(self, locator, expected_text, slicing=None):
        with allure.step(f"Wait for element located by {locator} to contain text '{expected_text}'"):
            element = self.wait.until(EC.presence_of_element_located(locator))
            actual_text = slicing(element.text) if slicing else element.text # Slicing operation on element text is expected
            assert expected_text.lower().strip() == actual_text.lower().strip(), f"Expected text '{expected_text}' but got '{actual_text}'"
            return element

    # Checks if the text of an alert contains the expected text
    def check_alert_text(self, actual_text, expected_text, slicing=None):
        with allure.step(f"Check if alert text contains '{expected_text}'"):
            actual_text = slicing(actual_text) if slicing else actual_text  # Slicing operation on alert text is expected
            assert expected_text == actual_text, f"Expected alert text '{expected_text}' but got '{actual_text}'"

    # Checks if the expected text is present in multiple elements
    def check_text_in_multiple_elements(self, locator, expected_text, slicing=None):
        with allure.step(f"Check if text '{expected_text}' is present in multiple elements"):
            elements = self.wait.until(EC.presence_of_all_elements_located(locator))
            for element in elements:
                actual_text = slicing(element.text) if slicing else element.text
                if str(expected_text).lower().strip() in actual_text.lower().strip():
                    return element
            assert False, f"Text '{expected_text}' not found in any of the elements"

    # Selects a random element from a list of elements that have valid text
    @staticmethod
    def get_random_text_element(elements):
        with allure.step("Get a random element from the list"):
            valid_elements = [element for element in elements if element.text.strip()]
            if not valid_elements:
                raise ValueError("No valid elements found")
            random_element = random.choice(valid_elements)
            allure.step(f"Selected element with text: '{random_element.text.strip()}'")
            return random_element

    # Selects a random element from a list of elements
    @staticmethod
    def get_random_element(elements):
        with allure.step("Get all elements from the list"):
            valid_elements = [element for element in elements]
            if not valid_elements:
                raise ValueError("No valid elements found")
            return random.choice(valid_elements)

    # Verifies that a specific text is not present in any of the provided element
    def verify_text_not_in_elements(self, elements, text_to_check):
        with allure.step(f"Verify that '{text_to_check}' is not present in the provided elements"):
            for element in elements:
                assert text_to_check not in element.text, f"Text '{text_to_check}' is still present in one of the elements."

    # Performs a double-click action on the given element
    def action_double_click(self, locator):
        with allure.step(f"Perform double-click action on the element located by {locator}"):
            action = ActionChains(self.driver)
            action.double_click(locator)
            action.perform()

    # Performs a right-click action on the given element
    def action_right_click(self, locator):
        with allure.step(f"Perform right-click action on the element located by {locator}"):
            action = ActionChains(self.driver)
            action.context_click(locator)
            action.perform()

    # Check when another tab opens
    def wait_for_new_tab(self):
        with allure.step("Wait for a new browser tab to be opened"):
            return self.wait.until(lambda d: len(d.window_handles) > 1)

    # Scrolls the page to a target element
    def scroll_to(self, target):
        if isinstance(target, tuple):  # Check if target is a locator
            element = self.driver.find_element(*target)
        else:  # Assumes target is a web element
            element = target
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    # Checks if an alert is present within the specified timeout
    def alert_is_present(self):
        with allure.step("Wait for alert to be present"):
            return self.wait.until(EC.alert_is_present())

    # Switch to alert
    def switch_to_alert(self):
        with allure.step("Switch to alert"):
            self.alert = self.driver.switch_to.alert

    # Entering the text in the alert
    def enter_text_to_alert(self, text):
        with allure.step("Entering the text in the alert"):
            self.alert.send_keys(text)

    # Verify that the text has changed
    def verify_change_text(self, previously_text, actual_text ):
        with allure.step(f"The change of text {previously_text} to {actual_text} was expected"):
            assert previously_text != actual_text, "The text has not changed"