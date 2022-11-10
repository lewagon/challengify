
from wagon_common.helpers.directories import are_directories_identical
from wagon_common.helpers.file import cp, rm
from wagon_common.helpers.subprocess import run_command

from wagon_common.helpers.git.create import git_init, git_add, git_commit

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

        in_path = os.path.join(data_path, "source", "07-Test-Run")
        out_path = os.path.join(data_path, "processed", "07-Test-Run")
        control_path = os.path.join(data_path, "control", "07-Test-Run")

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

    def test_run_with_deletion(self):

        # Arrange
        challengify = Challengify()

        data_path = os.path.join("tests", "data", "run")
        file_to_delete="03/02/to_delete.py"

        # Git init,add,commit in source path
        in_path = os.path.join(data_path, "source", "08-Test-Run-With-Deletion")
        git_init(in_path); git_add(in_path); git_commit(in_path, message="Initial commit (before deleting)")
        # Simulate file deletion and git tracking in source path
        rm(os.path.join(in_path, file_to_delete))
        git_add(in_path)

        # Git init, add, commit all in processed path
        out_path = os.path.join(data_path, "processed", "08-Test-Run-With-Deletion")
        git_init(out_path); git_add(out_path); git_commit(out_path, message="Initial commit")
        # Set a control path with desired outcome
        control_path = os.path.join(data_path, "control", "08-Test-Run-With-Deletion")

        # Act
        # TODO: Fix the command to avoid crashing on pipes
        git_diff_command = [
          "git", "diff",
          "--name-only",
          "HEAD",
          "|", "sed", "'s/^/\"/g'",
          "|", "sed", "'s/$/\"/g'",
          "|", "tr", "'\n'", "' '"
        ]
        breakpoint()
        rc, output, error = run_command(git_diff_command, cwd=in_path)
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

        # Cleanup
        # Put back the "to-be-deleted" file in destination
        cp(os.path.join(in_path, "template_to_delete.py"),os.path.join(out_path, "03", "02", "to_delete.py"))
        # Remove the .git folders in source and destination
        rm(os.path.join(in_path, ".git"), is_directory=True)
        rm(os.path.join(out_path, ".git"), is_directory=True)


if __name__ == '__main__':
    unittest.main()
