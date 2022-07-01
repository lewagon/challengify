from tests.functional.run.test_code_base import TestCodeBase

import unittest


class TestCodeProto(TestCodeBase):
    """
    basic tests to verify that the outcome of the transformation
    on code files does not change
    """

    def test_proto(self):
        """
        test python code file transformations
        """
        self.code_transformation_test("proto/code.proto")


if __name__ == '__main__':
    unittest.main()
