import random
import allure
from selenium.webdriver.support.select import Select
from base.base_page import BasePage
from config.urls import Urls


class DatePicker(BasePage):
    PAGE_URL = Urls.DATE_PICKER

    SELECT_DATE = ("xpath", "//input[@id='datePickerMonthYearInput']")
    SELECT_YEAR_CALENDAR = ("xpath", "//select[@class='react-datepicker__year-select']")
    SELECT_MONTH_CALENDAR = ("xpath", "//select[@class='react-datepicker__month-select']")
    SELECT_DAY_CALENDAR = ("xpath", "//div[@role='option']")
    MONTH_MAP = {
        "January": "01", "February": "02", "March": "03", "April": "04",
        "May": "05", "June": "06", "July": "07", "August": "08",
        "September": "09", "October": "10", "November": "11", "December": "12"
    }

    @allure.step("Select date in calendar")
    def select_date(self):
        self.element_is_clickable(self.SELECT_DATE).click()

        year_dropdown = self.element_is_presence(self.SELECT_YEAR_CALENDAR)
        select_year = Select(year_dropdown)
        years = select_year.options
        random_year_option = random.choice(years)
        self.year = random_year_option.text
        random_year_option.click()

        month_dropdown = self.element_is_presence(self.SELECT_MONTH_CALENDAR)
        select_month = Select(month_dropdown)
        months = select_month.options
        random_month_option = random.choice(months)
        self.month = random_month_option.text
        random_month_option.click()

        self.scroll_to(self.SELECT_DAY_CALENDAR)
        days = self.elements_are_presence(self.SELECT_DAY_CALENDAR)
        valid_days = [day for day in days if 1 <= int(day.text) <= 28]
        random_day_element = self.get_random_element(valid_days)
        self.day = random_day_element.text
        random_day_element.click()

    @allure.step("Verify date")
    def verify_date(self):
        numeric_month = self.MONTH_MAP[self.month]
        normalize_day = self.day.zfill(2)
        actual_date = f"{numeric_month}/{normalize_day}/{self.year}"
        self.check_element_value(self.SELECT_DATE, actual_date)