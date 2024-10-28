import allure
from base.base_page import BasePage
from config.urls import Urls


class Frames(BasePage):
    PAGE_URL = Urls.FRAMES

    IFRAME_1 = ("xpath", "//iframe[@id='frame1']")
    IFRAME_2 = ("xpath", "//iframe[@id='frame2']")
    TITLE_FRAME = ("css selector", 'h1[id="sampleHeading"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.result = None

    @allure.step("Switch to frame")
    def switching_to_iframe(self, frame_num):
        frame = self.element_is_presence(frame_num)
        width = frame.get_attribute('width')
        height = frame.get_attribute('height')
        self.driver.switch_to.frame(frame)
        text = self.element_is_presence(self.TITLE_FRAME).text
        self.driver.switch_to.default_content()
        self. result = [text, width, height]

    @allure.step("Check frame")
    def check_frame(self, expected_text):
        assert self.result == expected_text, f"Expected text '{expected_text}' but got '{self.result}'"
        self.driver.switch_to.default_content()


