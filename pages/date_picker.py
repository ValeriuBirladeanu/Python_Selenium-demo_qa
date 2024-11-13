from datetime import datetime
import random
import allure
from selenium.webdriver.support.select import Select
from base.base_page import BasePage
from config.urls import Urls


class DatePicker(BasePage):
    PAGE_URL = Urls.DATE_PICKER

    DATE_CALENDAR = ("xpath", "//input[@id='datePickerMonthYearInput']")
    YEAR_DATE_CALENDAR = ("xpath", "//select[@class='react-datepicker__year-select']")
    MONTH_DATE_CALENDAR = ("xpath", "//select[@class='react-datepicker__month-select']")
    DAY_DATE_CALENDAR = ("xpath", "//div[@role='option']")

    DATE_AND_TIME_CALENDAR = ("xpath", "//input[@id='dateAndTimePickerInput']")
    YEAR_DATE_AND_TIME_CALENDAR = ("xpath", "//div[contains(@class, 'year-dropdown-container--scroll')]")
    OPTION_YEAR_DATE_AND_TIME_CALENDAR = ("xpath", "//div[contains(@class, 'year-option')]")
    MONTH_DATE_AND_TIME_CALENDAR = ("xpath", "//div[contains(@class, 'month-dropdown-container--scroll')]")
    OPTIONS_MONTH_DATE_AND_TIME_CALENDAR = ("xpath", "//div[contains(@class, 'month-option')]")
    DAY_DATE_AND_TIME_CALENDAR = ("xpath", "//div[contains(@class, 'day react-datepicker')]")
    TIME_DATE_AND_TIME_CALENDAR = ("xpath", "//li[contains(@class, 'time-list-item ')]")

    MONTH_MAP = {
        "January": "01", "February": "02", "March": "03", "April": "04",
        "May": "05", "June": "06", "July": "07", "August": "08",
        "September": "09", "October": "10", "November": "11", "December": "12"
    }

    @allure.step("Select date in calendar")
    def select_date(self):
        self.element_is_clickable(self.DATE_CALENDAR).click()

        year_dropdown = self.element_is_presence(self.YEAR_DATE_CALENDAR)
        select_year = Select(year_dropdown)
        years = select_year.options
        random_year_option = random.choice(years)
        self.year = random_year_option.text
        random_year_option.click()

        month_dropdown = self.element_is_presence(self.MONTH_DATE_CALENDAR)
        select_month = Select(month_dropdown)
        months = select_month.options
        random_month_option = random.choice(months)
        self.month = random_month_option.text
        random_month_option.click()

        self.scroll_to(self.DAY_DATE_CALENDAR)
        days = self.elements_are_presence(self.DAY_DATE_CALENDAR)
        valid_days = [day for day in days if 1 <= int(day.text) <= 28]
        random_day_element = self.get_random_element(valid_days)
        self.day = random_day_element.text
        random_day_element.click()

    @allure.step("Verify date")
    def verify_date(self):
        numeric_month = self.MONTH_MAP[self.month]
        normalize_day = self.day.zfill(2)
        actual_date = f"{numeric_month}/{normalize_day}/{self.year}"
        self.check_element_value(self.DATE_CALENDAR, actual_date)

    @allure.step("Select date and time in calendar")
    def select_date_and_time(self):
        self.element_is_clickable(self.DATE_AND_TIME_CALENDAR).click()

        self.scroll_to(self.YEAR_DATE_AND_TIME_CALENDAR)
        self.element_is_clickable(self.YEAR_DATE_AND_TIME_CALENDAR).click()
        year_dropdown = self.elements_are_visible(self.OPTION_YEAR_DATE_AND_TIME_CALENDAR)
        random_year_option = self.get_random_element(year_dropdown)
        self.year = random_year_option.text
        random_year_option.click()

        self.scroll_to(self.MONTH_DATE_AND_TIME_CALENDAR)
        self.element_is_clickable(self.MONTH_DATE_AND_TIME_CALENDAR).click()
        month_dropdown = self.elements_are_visible(self.OPTIONS_MONTH_DATE_AND_TIME_CALENDAR)
        random_month_option = self.get_random_element(month_dropdown)
        self.month = random_month_option.text
        random_month_option.click()

        self.scroll_to(self.DAY_DATE_AND_TIME_CALENDAR)
        days = self.elements_are_presence(self.DAY_DATE_AND_TIME_CALENDAR)
        valid_days = [day for day in days if 1 <= int(day.text) <= 28]
        random_day_element = self.get_random_element(valid_days)
        self.day = random_day_element.text
        random_day_element.click()

        self.scroll_to(self.TIME_DATE_AND_TIME_CALENDAR)
        times = self.elements_are_presence(self.TIME_DATE_AND_TIME_CALENDAR)
        random_time_element = self.get_random_element(times)
        self.time = random_time_element.text
        random_time_element.click()

    @allure.step("Verify date and time")
    def verify_date_and_time(self):
        normalize_time = datetime.strptime(self.time, "%H:%M").strftime("%#I:%M %p").strip("✓")
        actual_date = f"{self.month} {self.day}, {self.year} {normalize_time}"
        self.get_updated_value(self.DATE_AND_TIME_CALENDAR)
        self.check_element_value(self.DATE_AND_TIME_CALENDAR, actual_date)