"""
called by the challengify command
runs injections in the solutions
"""

from wagon_sync.helpers.git import has_target_a_clean_git_status
from wagon_sync.action import run_actions


def run_inject(yaml_path):
    """
    verify git status of current directory
    run actions
    """

    # verify that current directory is a git repo and has a clean status
    if not has_target_a_clean_git_status("."):

        # cancel inject
        return

    # run actions
    run_actions(yaml_path)
