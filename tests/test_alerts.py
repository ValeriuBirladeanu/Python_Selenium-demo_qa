import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Alerts, Frame & Windows  - Alerts")
class TestAlerts(BaseTest):

    @allure.title("Click on the alert button")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_click_alert_button(self):
        self.alerts.open()
        self.alerts.is_opened()
        self.alerts.click_alert_button()
        self.alerts.check_opened_alert()
        self.alerts.accept_alert()

    @allure.title("Click on the 5 seconds alert button")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_click_five_seconds_alert_button(self):
        self.alerts.open()
        self.alerts.is_opened()
        self.alerts.click_five_seconds_alert_button()
        self.alerts.check_opened_five_seconds_alert()
        self.alerts.accept_alert()

    @allure.title("Click on confirm alert button")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_click_confirm_accept_alert_button(self):
        self.alerts.open()
        self.alerts.is_opened()
        self.alerts.click_confirm_alert_button()
        self.alerts.check_opened_confirm_alert()
        self.alerts.accept_alert()
        self.alerts.check_confirmed_text("You selected OK")

    @allure.title("Click on confirm alert button")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_click_confirm_dismiss_alert_button(self):
        self.alerts.open()
        self.alerts.is_opened()
        self.alerts.click_confirm_alert_button()
        self.alerts.check_opened_confirm_alert()
        self.alerts.dismiss_alert()
        self.alerts.check_confirmed_text("You selected Cancel")

    @allure.title("Click on input alert button")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_click_input_alert_button(self):
        self.alerts.open()
        self.alerts.is_opened()
        self.alerts.click_input_alert_button()
        self.alerts.check_opened_input_alert()
        self.alerts.enter_text_in_input_alert_button()
        self.alerts.accept_alert()
        self.alerts.check_opened_confirmed_text()