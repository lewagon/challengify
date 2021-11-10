
from wagon_sync.helpers.git import (
    has_target_a_clean_git_status,
    get_current_branch,
    checkout_branch)
from wagon_sync.action_copy import action_copy

import os

from colorama import Fore, Style


def action_clone(repo, branch, source, destination, command_destination):

    # verify that repo exists
    if not os.path.isdir(repo):

        print(Fore.RED
              + f"\nClone action repo {repo} is not a directory 🤕"
              + Style.RESET_ALL
              + "\nCannot proceed with clone action.")

        # cancel clone
        return

    # verify that repo has a clean git status
    if not has_target_a_clean_git_status(repo):

        # cancel clone
        return

    # retrieve previous branch
    previous_branch = get_current_branch(repo)

    # checkout branch
    checkout_branch(repo, branch)

    # build source
    source_path = os.path.join(
        repo,
        source)

    print(branch, end=" ")

    # copy content
    action_copy(source_path, destination, command_destination)

    # restore repo previous branch
    checkout_branch(repo, previous_branch)
