
from tests.functional.run.test_code_base import TestCodeBase

import unittest


class TestCodePython(TestCodeBase):
    """
    basic tests to verify that the outcome of the transformation
    on code files does not change
    """

    def test_python(self):
        """
        test python code file transformations
        """
        self.code_transformation_test("python/code.py")


if __name__ == '__main__':
    unittest.main()
