
from tests.functional.test_directories import are_directories_identical

from wagon_sync.challengify import Challengify
from wagon_sync.run_iterate import run_iterate

import unittest

import os
import shutil

from colorama import Fore, Style


class TestIterate(unittest.TestCase):
    """
    test that challenge versions are correctly generated from source codebase
    """

    def test_iterate(self):

        # Arrange
        challengify = Challengify()

        data_path = os.path.join("tests", "data", "iterate")

        in_path = os.path.join(data_path, "source")
        out_path = os.path.join(data_path, "processed")
        control_path = os.path.join(data_path, "control")

        # Act
        run_iterate(
            challengify=challengify,
            source=in_path,
            min_version=None,
            max_version=None,
            force=True,
            dry_run=False,
            verbose=True,
            ignore_metadata=False,
            format=False)

        # Assert
        rc, output, error = are_directories_identical(out_path, control_path)

        if rc != 0:

            print(Fore.RED
                  + "\nDirectory content does not match 🤕"
                  + Style.RESET_ALL
                  + f"\n- rc: {rc}"
                  + f"\n- output: {output}"
                  + f"\n- error: {error}")
            print(output.decode("utf-8"))

        assert rc == 0

        # Cleanup
        shutil.rmtree(out_path, ignore_errors=True)


if __name__ == '__main__':
    unittest.main()
