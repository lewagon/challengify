
from tests.functional.test_code_base import TestCodeBase

import unittest


class TestCodeHtml(TestCodeBase):
    """
    basic tests to verify that the outcome of the transformation
    on code files does not change
    """

    def test_html(self):
        """
        test html code file transformations
        """
        self.code_transformation_test("html/index.html")


if __name__ == '__main__':
    unittest.main()
