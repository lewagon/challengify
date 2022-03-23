
from tests.functional.run.test_code_base import TestCodeBase

import unittest


class TestCodeRuby(TestCodeBase):
    """
    basic tests to verify that the outcome of the transformation
    on code files does not change
    """

    def test_ruby(self):
        """
        test ruby code file transformations
        """
        self.code_transformation_test("ruby/code.rb")


if __name__ == '__main__':
    unittest.main()
