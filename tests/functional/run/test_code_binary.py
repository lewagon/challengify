
from tests.functional.run.test_binary_base import TestBinaryBase

import unittest


class TestCodeBinary(TestBinaryBase):
    """
    basic tests to verify that binary files matching a code file pattern
    are copied as is
    """

    def test_ds_store(self):
        """
        test binary files are copied as is
        """
        self.binary_transformation_test("binary/.DS_Store")


if __name__ == '__main__':
    unittest.main()
