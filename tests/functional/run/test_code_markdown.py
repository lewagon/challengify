
from tests.functional.run.test_code_base import TestCodeBase

import unittest


class TestCodeMarkdown(TestCodeBase):
    """
    basic tests to verify that the outcome of the transformation
    on code files does not change
    """

    def test_markdown(self):
        """
        test markdown code file transformations
        """
        self.code_transformation_test("markdown/test.md")


if __name__ == '__main__':
    unittest.main()
