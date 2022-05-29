
from tests.functional.run.test_code_base import TestCodeBase

import unittest


class TestCodeYml(TestCodeBase):
    """
    basic tests to verify that the outcome of the transformation
    on code files does not change
    """

    def test_yml(self):
        """
        test yaml code file transformations
        """
        for file in ["conf.yml",  "conf.yaml"]:
            self.code_transformation_test(f"yml/{file}")


if __name__ == '__main__':
    unittest.main()
