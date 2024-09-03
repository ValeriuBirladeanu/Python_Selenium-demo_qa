import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def open(self):
        with allure.step(f"Open {self.PAGE_URL} page"):
            self.driver.get(self.PAGE_URL)  # Opening the web page

    def is_opened(self):
        with allure.step(f"Page {self.PAGE_URL} is opened"):
            self.wait.until(EC.url_to_be(self.PAGE_URL))  # Checking if the web page has been opened

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