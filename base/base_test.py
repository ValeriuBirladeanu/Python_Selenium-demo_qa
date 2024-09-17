import pytest
from pages.text_box import TextBox
from pages.check_box import CheckBox
from pages.radio_button import RadioButton
from pages.web_tables import WebTables
from pages.buttons import Buttons
from pages.links import Links


class BaseTest:

    text_box: TextBox
    check_box: CheckBox
    radio_button: RadioButton
    web_tables: WebTables
    buttons: Buttons
    links: Links

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.text_box = TextBox(driver)
        request.cls.check_box = CheckBox(driver)
        request.cls.radio_button = RadioButton(driver)
        request.cls.web_tables = WebTables(driver)
        request.cls.buttons = Buttons(driver)
        request.cls.links = Links(driver)