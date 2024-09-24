import os.path

from seleniumbase import BaseCase

from pages.upload_page import UploadPage

from utils.helper import get_image_path

import pytest

from specs.base_test import BaseTest


class TestContactPage(BaseTest):
    @pytest.mark.smoke
    def test_single_file_upload(self):
        upload_page = UploadPage(self)
        upload_page.open()
        file_path = get_image_path("Test Screenshot.png")
        upload_page.upload_file(file_path)

    def test_multiple_file_upload(self):
        upload_page = UploadPage(self)
        upload_page.open()
        file_path_1 = get_image_path("Test Screenshot.png")

        file_path_2 = get_image_path("Test Screenshot 2.pdf")

        print(os.path.dirname(__file__))
        upload_page.upload_files([file_path_1, file_path_2])
