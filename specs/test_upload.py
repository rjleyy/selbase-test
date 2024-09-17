import os.path

from seleniumbase import BaseCase

from pages.upload_page import UploadPage

class TestContactPage(BaseCase):

    def test_single_file_upload(self):
        uploadpage = UploadPage(self)
        uploadpage.open()
        file_path = os.path.abspath('../data/Test Screenshot.png')
        file_input = uploadpage.single_input
        uploadpage.upload_file(file_path)

    def test_multiple_file_upload(self):
        uploadpage = UploadPage(self)
        uploadpage.open()
        file_path_1 = os.path.abspath('../data/Test Screenshot.png')
        file_path_2 = os.path.abspath('../data/Test Screenshot 2.pdf')
        uploadpage.upload_files([file_path_1, file_path_2])
