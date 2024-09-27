import os
import time
from PIL import Image, ImageDraw


class FileManager:

    def create_directory(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    def generate_image(self, directory, file_name, text):
        size = (200, 100)
        image = Image.new('RGB', size, color='white')
        ImageDraw.Draw(image).text((10, 10), text, fill='black')
        self.image_path = os.path.join(os.getcwd(), directory, file_name)
        image.save(self.image_path, format="PNG")
        return self.image_path

    def delete_image(self, directory=None):
        directory = directory or os.path.join(os.getcwd(), 'tests', 'downloads')
        assert os.path.exists(directory), f"The directory {directory} does not exist."
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            os.remove(file_path)
            assert not os.path.exists(file_path), f"Image {file_path} was not deleted."
        if os.listdir(directory):
            raise OSError(f"The directory {directory} is not empty after deletion.")

    def delete_directory(self, directory=None):
        time.sleep(5)
        directory = directory or self.directory
        if os.listdir(directory):
            raise OSError(f"The directory {directory} is not empty. It cannot be deleted.")
        os.rmdir(directory)
        assert not os.path.exists(directory), f"The directory {directory} was not deleted."