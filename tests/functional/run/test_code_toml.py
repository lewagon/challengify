
from tests.functional.run.test_code_base import TestCodeBase

import unittest


class TestCodeToml(TestCodeBase):
    """
    basic tests to verify that the outcome of the transformation
    on code files does not change
    """

    def test_yml(self):
        """
        test yaml code file transformations
        """
        self.code_transformation_test("toml/project.toml")


if __name__ == '__main__':
    unittest.main()
