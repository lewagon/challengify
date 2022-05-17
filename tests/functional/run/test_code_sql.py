
from tests.functional.run.test_code_base import TestCodeBase

import unittest


class TestCodeSql(TestCodeBase):
    """
    basic tests to verify that the outcome of the transformation
    on code files does not change
    """

    def test_sql(self):
        """
        test sql code file transformations
        """
        self.code_transformation_test("sql/query.sql")


if __name__ == '__main__':
    unittest.main()
