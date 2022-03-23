
from tests.functional.run.test_code_base import TestCodeBase

import unittest


class TestCodeJs(TestCodeBase):
    """
    basic tests to verify that the outcome of the transformation
    on code files does not change
    """

    def test_js(self):
        """
        test js code file transformations
        """
        self.code_transformation_test("js/app.js")


if __name__ == '__main__':
    unittest.main()
