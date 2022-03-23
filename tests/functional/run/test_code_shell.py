
from tests.functional.run.test_code_base import TestCodeBase

import unittest


class TestCodeShell(TestCodeBase):
    """
    basic tests to verify that the outcome of the transformation
    on code files does not change
    """

    def test_shell(self):
        """
        test shell code file transformations
        """
        for file in [".zshrc",  "Dockerfile",  "Makefile",  "script.sh"]:
            self.code_transformation_test(f"shell/{file}")


if __name__ == '__main__':
    unittest.main()
