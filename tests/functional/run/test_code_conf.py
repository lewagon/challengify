
from tests.functional.run.test_code_base import TestCodeBase

import unittest


class TestCodeConf(TestCodeBase):
    """
    basic tests to verify that the outcome of the transformation
    on code files does not change
    """

    def test_conf(self):
        """
        test conf code file transformations
        """
        self.code_transformation_test("conf/.conf")


if __name__ == '__main__':
    unittest.main()
