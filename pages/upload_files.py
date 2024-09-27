import os
import allure
from base.base_page import BasePage
from config.urls import Urls
from data.data_generator import TestDataGenerator
from file_management.file_manager import FileManager


class UploadFiles(BasePage):
    PAGE_URL = Urls.UPLOAD_FILES

    CHOOSE_FILE_BUTTON = ("xpath", "//input[@id='uploadFile']")
    UPDATED_FILE_TEXT = ("xpath", "//p[@id='uploadedFilePath']")

    def __init__(self, driver):
        super().__init__(driver)
        self.data_generator = TestDataGenerator()
        self.file_manager = FileManager()
        self.directory = os.path.join(os.getcwd(), 'downloads')
        self.fail_name = self.data_generator.generate_png_fail_name()

    @allure.step("Create directory for uploads")
    def create_directory(self):
        self.file_manager.create_directory(self.directory)

    @allure.step("Sending the generated file")
    def upload_file(self):
        text = self.data_generator.generate_text()
        file_path = self.file_manager.generate_image(self.directory, self.fail_name, text)
        self.element_is_presence(self.CHOOSE_FILE_BUTTON).send_keys(file_path)

    @allure.step("Verify uploaded file")
    def verify_uploaded_file(self):
        self.check_element_text(self.UPDATED_FILE_TEXT, self.fail_name, lambda slicing: slicing.split("\\")[-1])

    @allure.step("Delete generated image")
    def delete_image(self):
        self.file_manager.delete_image(self.directory)

    @allure.step("Delete generated directory")
    def delete_directory(self):
        self.file_manager.delete_directory(self.directory)