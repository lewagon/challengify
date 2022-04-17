
from wagon_sync.challengify import Challengify
from wagon_sync.run_iterate import run_iterate

from wagon_common.tests.base.directory_equality import TestBaseDirectoryEquality

import os


class TestIterate(TestBaseDirectoryEquality):
    """
    test that challenge versions are correctly generated from source codebase
    """

    def test_iterate(self):

        # Arrange
        tests_root = os.path.join("tests", "data")

        challengify = Challengify()

        # Act
        def act():

            run_iterate(
                challengify=challengify,
                source=self.source_root,
                min_version=None,
                max_version=None,
                force=True,
                dry_run=False,
                verbose=True,
                ignore_metadata=False,
                format=False)

        # Assert
        self.run_test_directory_identical(
            os.path.join(
                tests_root, "iterate"),
            act)

        # Cleanup
