import os

def assert_list_text(base_case, list_selector, expected_text):
    """
    Verifies the text of each element in a list that matches the expected text
    :param base_case: Instance of BaseCase
    :param list_selector: CSS Selector for the list elements
    :param expected_text: List of expected text for each element
    :return:

    Example:
    assert_list_text(base_case, ".menu-item", ["Home", "About"])
    """
    for i, text in enumerate(expected_text, start=1):
        base_case.assert_text(text, f'{list_selector}:nth-child({i})')

def get_image_path(file_name):
    """
    Helper function to get the absolute file path of an image file in the data folder

    :param file_name: Name of the file you want the path for
    :return: returns the absolute path of the file
    """
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'data', file_name, )
    )