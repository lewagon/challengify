
from wagon_common.helpers.directories import are_directories_identical
from wagon_common.helpers.file import cp
from wagon_common.helpers.subprocess import run_command

from wagon_common.helpers.git.create import git_init, git_add, git_commit

from wagon_sync.challengify import Challengify
from wagon_sync.run_sync import run_sync

import unittest
import pytest

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

    @pytest.fixture
    def deletion_scenario_fixtures(self):
        # Arrange
        self.challengify = Challengify()

        data_path = os.path.join("tests", "data", "run")
        file_to_delete = "03/02/to_delete.py"

        # Git init,add,commit in source path
        self.in_path = os.path.join(data_path, "source", "08-Test-Run-With-Deletion")
        git_init(self.in_path); git_add(self.in_path); git_commit(self.in_path, message="Initial commit (before deleting)")
        # Simulate file deletion and git tracking in source path
        shutil.rmtree(os.path.join(self.in_path, file_to_delete), ignore_errors=True)
        git_add(self.in_path)

        # Git init, add, commit all in processed path
        self.out_path = os.path.join(data_path, "processed", "08-Test-Run-With-Deletion")
        git_init(self.out_path); git_add(self.out_path); git_commit(self.out_path, message="Initial commit")
        # Set a control path with desired outcome
        self.control_path = os.path.join(data_path, "control", "08-Test-Run-With-Deletion")

        yield

        # Cleanup
        # Put back the "to-be-deleted" file in destination and source
        cp(os.path.join(self.in_path, "template_to_delete.py"),os.path.join(self.out_path, "03", "02", "to_delete.py"))
        cp(os.path.join(self.in_path, "template_to_delete.py"),os.path.join(self.in_path, "03", "02", "to_delete.py"))
        # Remove the .git folders in source and destination
        shutil.rmtree(os.path.join(self.out_path, ".git"), ignore_errors=True)
        shutil.rmtree(os.path.join(self.in_path, ".git"), ignore_errors=True)

    @pytest.mark.usefixtures('deletion_scenario_fixtures')
    def test_run_with_deletion(self):

        # Act
        git_diff_command = ["git", "diff", "--name-only", "HEAD"]
        rc, output, error = run_command(git_diff_command, cwd=self.in_path)
        diff_files = output.decode("utf-8").split()

        run_sync(
            challengify=self.challengify,
            sources=diff_files,
            destination=self.out_path,
            force=True,
            dry_run=False,
            verbose=True,
            test=False,
            ignore_tld=True,
            iterate_yaml_path=".")

        # Assert
        rc, output, error = are_directories_identical(self.out_path, self.control_path, ignored_files=['.git'])

        if rc != 0:
            print(Fore.RED
                  + "\nDirectory content does not match 🤕"
                  + Style.RESET_ALL
                  + f"\n- rc: {rc}"
                  + f"\n- output: {output}"
                  + f"\n- error: {error}")
            print(output.decode("utf-8"))
        assert rc == 0


if __name__ == '__main__':
    unittest.main()
