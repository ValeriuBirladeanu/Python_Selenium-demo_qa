import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Elements - Broken_Links_Images")
class TestBrokenLinksImages(BaseTest):

    @allure.title("Test valid image is displayed correctly")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_valid_image(self):
        self.broken_links_images.open()
        self.broken_links_images.is_opened()
        self.broken_links_images.check_valid_image()

    @allure.title("Test broken image is not displayed")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_broken_image(self):
        self.broken_links_images.open()
        self.broken_links_images.is_opened()
        self.broken_links_images.check_broken_image()

    @allure.title("Verify opening valid link")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_open_valid_link(self):
        self.broken_links_images.open()
        self.broken_links_images.is_opened()
        self.broken_links_images.click_valid_link()
        self.broken_links_images.check_opened_valid_link()

    @allure.title("Verify opening broken link")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_open_broken_link(self):
        self.broken_links_images.open()
        self.broken_links_images.is_opened()
        self.broken_links_images.click_broken_link()
        self.broken_links_images.check_opened_broken_link()