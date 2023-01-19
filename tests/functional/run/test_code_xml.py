
from tests.functional.run.test_code_base import TestCodeBase

import unittest


class TestCodeYml(TestCodeBase):
    """
    basic tests to verify that the outcome of the transformation
    on code files does not change
    """

    def test_xml(self):
        """
        test xml code file transformations
        """
        self.code_transformation_test("xml/users.xml")


if __name__ == '__main__':
    unittest.main()
