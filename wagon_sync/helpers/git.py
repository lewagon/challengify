"""
git cli helper
"""

from wagon_common.helpers.subprocess import run_command

from colorama import Fore, Style


def has_target_a_clean_git_status(path):

    # retrieve git status
    command = [
        "git",
        "status",
        ]

    rc, output, error = run_command(command, cwd=path, verbose=False)

    # checking that target is a git repo
    if rc != 0:

        if "not a git repository" in error.decode("utf-8"):

            print(Fore.RED
                  + f"\nDestination {path} is not a git repository 🤕"
                  + Style.RESET_ALL
                  + "\nThe command can either be run with a destination that does not exist"
                  + "\nor with a destination that is a git repo with a clean status.")

        else:

            print(Fore.RED
                  + f"\nError getting destination {path} git status 😵"
                  + Style.RESET_ALL
                  + "\nThe command can either be run with a destination that does not exist"
                  + "\nor with a destination that is a git repo with a clean status.")

        return False

    # decode output
    lines = output.decode("utf-8").strip().split("\n")

    # checking that git status is clean
    if ("nothing to commit, working tree clean" not in lines and
        "nothing to commit (create/copy files and use \"git add\" to track)" not in lines):

        print(Fore.RED
              + f"\nDestination {path} does not have a clean git status 🤒"
              + Style.RESET_ALL
              + "\nPlease commit any changes before running this command.")

        return False

    # destination is a git repo with clean status
    return True


def get_current_branch(path):

    # retrieve current branch
    command = [
        "git",
        "branch",
        "--show-current",
        ]

    _rc, output, _error = run_command(command, cwd=path, verbose=False)

    # return current branch
    return output.decode("utf-8")


def checkout_branch(path, branch):

    # retrieve current branch
    command = [
        "git",
        "checkout",
        branch,
        ]

    _rc, _output, _error = run_command(command, cwd=path, verbose=False)
