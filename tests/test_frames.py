import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Alerts, Frame & Windows  - Frames")
class TestFrames(BaseTest):

    @allure.title("Click on the alert button")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_iframe(self):
        self.frames.open()
        self.frames.is_opened()
        self.frames.switching_to_iframe(self.frames.IFRAME_1)
        expected_text_1 = ['This is a sample page', '500px', '350px']
        self.frames.check_frame(expected_text_1)
        self.frames.switching_to_iframe(self.frames.IFRAME_2)
        expected_text_2 = ['This is a sample page', '100px', '100px']
        self.frames.check_frame(expected_text_2)