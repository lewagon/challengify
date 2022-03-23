
from tests.functional.test_code_base import TestCodeBase

import unittest


class TestCodeRails(TestCodeBase):
    """
    basic tests to verify that the outcome of the transformation
    on code files does not change
    """

    def test_rails(self):
        """
        test rails code file transformations
        """
        for file in ["view.html.erb",  "view.js.erb"]:
            self.code_transformation_test(f"rails/{file}")


if __name__ == '__main__':
    unittest.main()
