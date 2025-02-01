import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Elements - Upload Files")
class TestUploadFiles(BaseTest):

    @allure.title("Test uploaded file")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_uploaded_file(self):
        self.upload_files.open()
        self.upload_files.is_opened()
        self.upload_files.create_directory()
        self.upload_files.upload_file()
        self.upload_files.verify_uploaded_file()
        self.upload_files.delete_image()
        self.upload_files.delete_directory()