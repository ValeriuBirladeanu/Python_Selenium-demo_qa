import pytest

from pages.text_box import TextBox
from pages.check_box import CheckBox


class BaseTest:

    text_box: TextBox
    check_box: CheckBox

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.text_box = TextBox(driver)
        request.cls.check_box = CheckBox(driver)