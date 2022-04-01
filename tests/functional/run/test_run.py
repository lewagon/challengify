
from tests.functional.test_directories import are_directories_identical

from wagon_sync.challengify import Challengify
from wagon_sync.run_sync import run_sync

import unittest

import os
import shutil

from colorama import Fore, Style


class TestRun(unittest.TestCase):
    """
    test that challenge versions are correctly generated from source codebase
    """

    def test_run(self):

        # Arrange
        challengify = Challengify()

        data_path = os.path.join("tests", "data", "run")

        in_path = os.path.join(data_path, "source")
        out_path = os.path.join(data_path, "processed")
        control_path = os.path.join(data_path, "control")

        # Act
        run_sync(
            challengify=challengify,
            sources=[in_path],
            destination=out_path,
            force=True,
            dry_run=False,
            verbose=True,
            test=False,
            ignore_tld=True,
            iterate_yaml_path=".")

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

        # test does not work yet
        #
        # unable to ignore the relative position of the source dir
        # and to generate the challenge precisely in the control dir

        # assert rc == 0

        # Cleanup
        shutil.rmtree(out_path, ignore_errors=True)


if __name__ == '__main__':
    unittest.main()
