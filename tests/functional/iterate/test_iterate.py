
from wagon_sync.challengify import Challengify
from wagon_sync.run_iterate import run_iterate

import unittest

import os

from wagon_common.helpers.subprocess import run_command

from colorama import Fore, Style


def are_directories_identical(directory_a, directory_b):
    """
    recursively compare directory structure and file content
    """

    # compare directories
    command = [
        "diff",
        "-r",
        directory_a,
        directory_b]

    rc, output, error = run_command(command, verbose=False)

    return rc, output, error


class TestIterate(unittest.TestCase):
    """
    test that challenge versions are correctly generated from source codebase
    """

    def test_iterate(self):

        # Arrange
        challengify = Challengify()

        in_path = os.path.join(
            os.path.dirname(__file__), "..", "..", "data", "iterate", "source")

        out_path = os.path.join(
            os.path.dirname(__file__), "..", "..", "data", "iterate", "processed")

        control_path = os.path.join(
            os.path.dirname(__file__), "..", "..", "data", "iterate", "control")

        # Act
        run_iterate(
            challengify=challengify,
            source=in_path,
            min_version=None,
            max_version=None,
            force=True,
            dry_run=False,
            verbose=False,
            ignore_metadata=False,
            format=False)

        # Assert
        rc, output, error = are_directories_identical(out_path, control_path)

        if rc != 0:

            print(Fore.RED
                  + "\nDirectories content does not match 🤕"
                  + Style.RESET_ALL
                  + f"\n- rc: {rc}"
                  + f"\n- output: {output}"
                  + f"\n- error: {error}")
            print(output.decode("utf-8"))

        assert rc == 0

        # Cleanup


if __name__ == '__main__':
    unittest.main()
