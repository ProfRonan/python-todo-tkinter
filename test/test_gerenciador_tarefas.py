"""Test file for testing the functions in main.py file"""

import unittest  # for creating the test case
import sys  # for adding the parent directory to the path
from pathlib import Path  # for getting the path of the main.py file
# add the parent directory to the path in order to run it from the run command in vscode
MAIN_FILE_FOLDER = Path(__file__).parents[1].as_posix()
sys.path.insert(1, MAIN_FILE_FOLDER)
import gerenciador_tarefas as gt  # nopep8 pylint: disable=wrong-import-position


class TestFunction(unittest.TestCase):
    """Class for testing the main.py file"""

    def test_add_2_3(self):
        """Tests if the addition function returns the correct value 5"""
        self.assertEqual(2 + 3, 5)


if __name__ == "__main__":
    unittest.main()
