
from tests.functional.run.test_code_base import TestCodeBase

import unittest


class TestCodeCss(TestCodeBase):
    """
    basic tests to verify that the outcome of the transformation
    on code files does not change
    """

    def test_css(self):
        """
        test css code file transformations
        """
        self.code_transformation_test("css/main.css")


if __name__ == '__main__':
    unittest.main()
