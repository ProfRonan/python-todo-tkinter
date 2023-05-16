"""Test file for testing the main.py file"""

import unittest  # for creating the test case
from unittest.mock import patch  # for mocking the input
import io  # for capturing the output
import sys  # for restoring the stdout and removing the main module from the cache
import importlib  # for importing the main.py file
from pathlib import Path  # for getting the path of the main.py file
# add the parent directory to the path in order to run it from the run command in vscode
MAIN_FILE_FOLDER = Path(__file__).parents[1].as_posix()
sys.path.insert(1, MAIN_FILE_FOLDER)


class TestMain(unittest.TestCase):
    """Class for testing the main.py file"""

    def setUp(self):
        """Sets up the test environment by removing the main module from the cache"""
        super().setUp()
        sys.modules.pop("main", None)

    @patch("builtins.input", return_value="John")
    def test_prints_hello_name(self, _mock_input):
        """Tests if the main.py file prints the correct output"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Hello John!")

    @patch("builtins.input", return_value="Mathew")
    def test_prints_hello_other_name(self, _mock_input):
        """Tests if the main.py file prints the correct output"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Hello Mathew!")


if __name__ == "__main__":
    unittest.main()
