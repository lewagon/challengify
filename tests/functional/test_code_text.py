
from tests.functional.test_code_base import TestCodeBase

import unittest


class TestCodeActions(TestCodeBase):
    """
    basic tests to verify that the outcome of the transformation
    on code files does not change
    """

    def test_text(self):
        """
        test text code file transformations
        """
        self.code_transformation_test("txt/requirements.txt")


if __name__ == '__main__':
    unittest.main()
