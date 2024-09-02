import pytest

from pages.text_box import TextBox


class BaseTest:

    text_box: TextBox

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.text_box = TextBox(driver)