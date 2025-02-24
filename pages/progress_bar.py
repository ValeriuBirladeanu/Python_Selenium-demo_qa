import allure
from base.base_page import BasePage
from config.urls import Urls


class Progress_Bar(BasePage):
    PAGE_URL = Urls.PROGRESS_BAR

    PROGRESS_BAR_VALUE = ("xpath", '//div[@id="progressBar"]')
    PROGRESS_BAR_BUTTON = ("xpath", '//button[@id="startStopButton"]')

    @allure.step("Click on progress bar button and apply random wait before second click")
    def change_progress_bar_value(self):
        self.value_before = self.element_is_visible(self.PROGRESS_BAR_VALUE).text
        progress_bar = self.element_is_clickable(self.PROGRESS_BAR_BUTTON)
        progress_bar.click()
        self.wait_for_random_time(2, 5)
        progress_bar.click()
        self.value_after = self.element_is_visible(self.PROGRESS_BAR_VALUE).text

    @allure.step("Click on progress bar button multiple times with random wait between clicks")
    def change_progress_bar_value_multiple_clicks(self):
        self.value_before = self.element_is_visible(self.PROGRESS_BAR_VALUE).text
        progress_bar = self.element_is_clickable(self.PROGRESS_BAR_BUTTON)
        progress_bar.click()
        self.wait_for_random_time(1, 5)
        progress_bar.click()
        self.wait_for_random_time(1, 2)
        progress_bar.click()
        self.wait_for_random_time(1, 5)
        progress_bar.click()
        self.value_after = self.element_is_visible(self.PROGRESS_BAR_VALUE).text

    @allure.step("Verify progress bar value change after STOP button click")
    def check_progres_bar_value_change(self):
        self.verify_value_change(self.value_before, self.value_after)