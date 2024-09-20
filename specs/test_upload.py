import os.path

from seleniumbase import BaseCase

from pages.upload_page import UploadPage


class TestContactPage(BaseCase):

    def test_single_file_upload(self):
        upload_page = UploadPage(self)
        upload_page.open()
        file_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'data', 'Test Screenshot.png',))

        upload_page.upload_file(file_path)

    def test_multiple_file_upload(self):
        upload_page = UploadPage(self)
        upload_page.open()
        file_path_1 = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'data', 'Test Screenshot.png',)
        )
        file_path_2 = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'data', 'Test Screenshot 2.pdf',)

        )
        print(os.path.dirname(__file__))
        upload_page.upload_files([file_path_1, file_path_2])
