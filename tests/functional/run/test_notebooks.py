
from wagon_sync.challengify import Challengify

from wagon_sync.process_notebook import process_notebook

import unittest
# import inspect

import os
import re


class TestNotebookActions(unittest.TestCase):
    """
    basic tests to verify that the outcome of the transformation
    on notebook files does not change appart from the generated `id` attributes
    """

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.challengify = Challengify()

    def __transformation_test(self, caller_name):

        # retrieve caller name
        # caller_name = inspect.currentframe().f_back.f_code.co_name

        # get notebook path
        in_nb = os.path.join(os.path.dirname(__file__), "..", "..", "data", "notebooks", caller_name, "notebook_in.ipynb")
        processed_nb = os.path.join(os.path.dirname(__file__), "..", "..", "data", "notebooks", caller_name, "notebook_challengify.ipynb")

        # format python code
        process_notebook(
            self.challengify,
            in_nb, processed_nb, ".ipynb")

        # load notebooks
        out_nb = os.path.join(os.path.dirname(__file__), "..", "..", "data", "notebooks", caller_name, "notebook_out.ipynb")

        with open(out_nb, "r") as file:
            out_data = file.read()

        with open(processed_nb, "r") as file:
            processed_data = file.read()

        # compare results
        pattern = r'"id": "[^"]*"'
        out_raw = re.sub(pattern, "", out_data)
        processed_raw = re.sub(pattern, "", processed_data)

        # remove processed file
        os.remove(processed_nb)

        self.assertEqual(out_raw, processed_raw)

    def test_clean_notebook_output(self):
        """
        clean the output of all notebook cells
        notebook has a filled metadata
        """
        self.__transformation_test("clean_notebook_output")

    def test_clean_cleaned_notebook_output(self):
        """
        clean the output of all notebook cells
        notebook metadata has been cleaned by nbcleanmeta
        """
        self.__transformation_test("clean_cleaned_notebook_output")

    def test_clean_notebook_stderr(self):
        """
        clean the stderr of all notebook cells
        notebook has a filled metadata
        """
        self.__transformation_test("clean_notebook_stderr")

    def test_clean_cleaned_notebook_stderr(self):
        """
        clean the stderr of all notebook cells
        notebook metadata has been cleaned by nbcleanmeta
        """
        self.__transformation_test("clean_cleaned_notebook_stderr")

    def test_clean_cells_with_clean_tag(self):
        """
        only clean the output and stderr of cells with corresponding tag
        """
        self.__transformation_test("clean_cells_with_clean_tag")

    def test_delete_cells_with_delete_tag(self):
        self.__transformation_test("delete_cells_with_delete_tag")

    def test_delete_content_surrounded_by_delete_delimiters(self):
        self.__transformation_test("delete_content_surrounded_by_delete_delimiters")

    def test_replace_content_surrounded_by_challengify_delimiters(self):
        self.__transformation_test("replace_content_surrounded_by_challengify_delimiters")


if __name__ == '__main__':
    unittest.main()
