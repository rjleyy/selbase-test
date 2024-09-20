from seleniumbase import BaseCase
from config.default import BASE_URL


class UploadPage:

    def __init__(self, sb: BaseCase):

        # Locators
        self.sb = sb
        self.single_input = ".single input"
        self.multi_input = ".multiple input"
        self.preview = ".preview img"
        self.upload_button = ".cart-main-area button"
        self.toast_success = ".react-toast-notifications__toast__content"

    def open(self):
        self.sb.open(f"{BASE_URL}/upload")

        # using an underscore means that this is a private method

    def _upload_all(self, file_selector, file_path):
        """
        Uploads file(s) using the specified input selector(s) and file path(s)

        :param file_selector: file input element
        :param file_path: path of the file you want uplaoded
        """
        self.sb.choose_file(file_selector, file_path)
        self.sb.assert_element(self.preview)
        self.sb.click(self.upload_button)

    def upload_file(self, file_path):
        self._upload_all(self.single_input, file_path)
        self.sb.assert_text("Image uploaded successfully", self.toast_success)

    def upload_files(self, file_paths):
        """
        Uploads file(s) using the specified input selector(s) and file path(s)

        :param file_selector: file input element
        :param file_path: path of the file you want uploaded
        """
        multiple_file_paths = "\n".join(file_paths)
        self._upload_all(self.multi_input, multiple_file_paths)
        self.sb.assert_text("Images uploaded successfully", self.toast_success)
