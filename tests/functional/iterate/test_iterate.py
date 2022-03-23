
from wagon_sync.challengify import Challengify
from wagon_sync.run_iterate import run_iterate

import unittest

import os


class TestIterate(unittest.TestCase):
    """
    test that challenge versions are correctly generated from source codebase
    """

    def test_iterate(self):

        # Arrange
        challengify = Challengify()

        source_path = os.path.join(
            os.path.dirname(__file__), "..", "..", "data", "iterate", "source")

        # Act
        run_iterate(
            challengify=challengify,
            source=source_path,
            min_version=None,
            max_version=None,
            force=True,
            dry_run=False,
            verbose=True,
            ignore_metadata=False,
            format=False)

        # Assert
        assert False

        # Cleanup


if __name__ == '__main__':
    unittest.main()
