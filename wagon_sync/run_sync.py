"""
called by the challengify command
runs sync on specified sources
"""

from wagon_sync.challengify import Challengify

from wagon_sync.helpers.filter import (
    list_files_matching_dirs,
    list_files_matching_pattern)
from wagon_sync.helpers.git import has_target_a_clean_git_status
from wagon_sync.process import process
from wagon_sync.params.sync import UNSYNCED_PATTERN
from wagon_sync.autoformat import autoformat_code

from wagon_common.helpers.scope import resolve_scope
from wagon_common.helpers.output import print_files
from wagon_common.helpers.git.repo import get_git_top_level_directory, git_rm_and_clean


import glob

import os
import shutil

from colorama import Fore, Style

SYNC_IGNORE_PATH = ".syncignore"
CHALLENGIFY_IGNORE_PREFIX = ".challengifyignore"


def get_root_and_rel_path():
    """ return current working directory path relative to project root """

    # retrieve project root
    tld = get_git_top_level_directory()

    # get current directory
    cwd = os.getcwd()

    # get current directory path relatively to project root
    relative_path = os.path.relpath(cwd, tld)

    return tld, relative_path


def get_destination_cwd(destination):
    """ corrects destination relatively to current working directory """

    # get relative path
    tld, relative_path = get_root_and_rel_path()

    # build target path
    target = os.path.join(tld, destination, relative_path)

    # get absolute path
    abs_target = os.path.abspath(target)

    return abs_target


def get_iterate_destination_cwd(destination, iterate_yaml_path):
    """ corrects destination relatively to tld """

    # retrieve project root
    tld = get_git_top_level_directory()

    # build target path
    target = os.path.join(tld, iterate_yaml_path, destination)

    # get absolute path
    abs_target = os.path.abspath(target)

    return abs_target


def load_ignored_files():
    """
    return the set of ignored files
    """

    # get relative path
    tld, relative_path = get_root_and_rel_path()

    # build challengify ignore path
    cha_ignore_path = os.path.join(tld, "**", CHALLENGIFY_IGNORE_PREFIX + "*")

    # build sync ignore path
    sync_ignore_path = os.path.join(tld, SYNC_IGNORE_PATH)

    # list challengify ignore files
    cha_ignore_files = (
        glob.glob(sync_ignore_path, recursive=True)
        + glob.glob(cha_ignore_path, recursive=True))

    # iterate through ignore files
    ignored = []

    for ignore_file_path in cha_ignore_files:

        # reading non empty ignored entries
        with open(ignore_file_path) as file:

            # retrieve ignore file parent path
            ignore_parent_path = os.path.relpath(
                os.path.dirname(ignore_file_path), start=tld)

            # ignore empty lines and comments (lines starting with #)
            ignored += [os.path.join(ignore_parent_path, e) for e in [l.strip() for l in file] if e != "" and e[:1] != "#"]

    # expand ignored paths
    expanded_ignored = [os.path.relpath(expanded) for path in ignored for expanded in glob.glob(os.path.relpath(path, relative_path), recursive=True)]

    # deduplicate paths
    return sorted(set(expanded_ignored))


def run_sync(
        challengify: Challengify,
        sources,
        destination,
        force,
        dry_run,
        verbose,
        test,
        user_autoformater=False,        # autoformat generated code
        ignore_tld=False,               # ignore current path in git directory
        iterate_yaml_path=None,         # path to iterate yaml
        additional_ignores=[],          # ignored files and preprocessing
        custom_files=[],                # list of custom target files
        version_iterator=None,          # for the challengify iterate command
        version_info=None,              # version info for challengify iterate
        from_scratch=False):            # whether to delete all files in destination before sync
    """
    iterate through sources
    expand source path
    filter out git ignored files
    synchronize source
    """

    # correct destination tld
    if ignore_tld:

        # challengify iterate
        destination = get_iterate_destination_cwd(destination, iterate_yaml_path)

    else:

        # challengify run
        destination = get_destination_cwd(destination)

    # verify that destination directory does not exist
    # or is a git repo and has a clean status
    # or sync is forced
    if not force \
       and not test \
       and os.path.isdir(destination) \
       and not has_target_a_clean_git_status(destination):

        # cancel sync
        return

    # if --from-scratch, delete all files in destination
    if from_scratch:

        print(Fore.RED
              + f"\nDeleting all files in destination directory: {destination}"
              + Style.RESET_ALL)

        rm_and_clean_success = git_rm_and_clean(path=destination, verbose=verbose)

        if not rm_and_clean_success:

            # cancel sync
            print(Fore.RED
                  + f"\nError while wiping destination git directory. Sync cancelled ❌"
                  + Style.RESET_ALL
                  + f"\n- destination: {destination}")

            return

    version_info = f" ({version_info})" if version_info is not None else ""

    # correct scope
    if ignore_tld:

        # correct scope path relative to iterate yaml path
        sources = [os.path.join(iterate_yaml_path, source) for source in sources]

    # retrieve git controlled files in scope
    controlled_files, deleted_files = resolve_scope(sources, ["*"], return_inexisting=True, verbose=verbose)

    # delete files in destination if they exist
    processed_deleted_files = []
    for deleted_file in deleted_files:
        deleted_file_at_destination = os.path.join(destination, deleted_file)
        if os.path.isfile(deleted_file_at_destination):
            os.remove(deleted_file_at_destination)
            processed_deleted_files.append(deleted_file_at_destination)
        elif os.path.isdir(deleted_file_at_destination):
            shutil.rmtree(deleted_file_at_destination)
            processed_deleted_files.append(deleted_file_at_destination)

    if verbose:
        print_files("red", f"Files deleted in destination {destination}", processed_deleted_files)

    # 🔥 TODO: return list of deleted files to caller in addition to original_files, corrected_files ([], [] if no git controlled files are found)

    controlled_files = controlled_files[0]

    if not controlled_files:

        print(Fore.RED
              + f"\nNo files controlled by git in the scope{version_info} 😶‍🌫️"
              + Style.RESET_ALL
              + "\nPlease make sure to `git add` any files that you want to challengify")
        return [], []

    # retrieve sync ignored files
    ignored_files = load_ignored_files()

    if verbose:
        print_files("blue", f"Files in {SYNC_IGNORE_PATH}", ignored_files)

    # exclude ignored files
    scope_ignored_files = sorted(set(controlled_files) & set(ignored_files))
    candidate_files = sorted(set(controlled_files) - set(ignored_files))

    if verbose:
        print_files("red", f"Files excluded by {SYNC_IGNORE_PATH} files", scope_ignored_files)

    # exclude ignored directories
    excluded_files = list_files_matching_dirs(candidate_files, ignored_files)
    candidate_files = sorted(set(candidate_files) - set(excluded_files))

    if verbose:
        print_files("red", f"Files excluded by {SYNC_IGNORE_PATH} directories", excluded_files)

    # exclude files matching unsynced pattern
    excluded_files = list_files_matching_pattern(candidate_files, UNSYNCED_PATTERN)
    candidate_files = sorted(set(candidate_files) - set(excluded_files))

    if verbose:
        print_files("red", f"Files excluded by {UNSYNCED_PATTERN} pattern", excluded_files)

    # exclude additional ignores required by the challengify iterate command
    candidate_files = sorted(set(candidate_files) - set(additional_ignores))

    if verbose:
        print_files("red", "Files excluded by challengify iterate", additional_ignores)

    print_files("green", "Files candidate", candidate_files)

    if dry_run:
        print(Fore.BLUE
              + f"\nDry run on files{version_info}:"
              + Style.RESET_ALL)
    else:
        print(Fore.GREEN
              + f"\nCopy files{version_info}:"
              + Style.RESET_ALL)

    # synchronize files
    corrected_files = []
    original_files = []

    for candidate_file in candidate_files:

        # resolve custom files
        if candidate_file in custom_files:
            destination_filepath = custom_files[candidate_file]
        else:
            destination_filepath = candidate_file

        # synchronize file
        destination_file_path, destination_path = process(
            challengify,
            candidate_file, destination, destination_filepath, dry_run,
            ignore_tld=ignore_tld, iterate_yaml_path=iterate_yaml_path,
            test=test,
            version_iterator=version_iterator)

        # append corrected files
        corrected_files.append(destination_path)
        original_files.append(destination_file_path)

    # autoformat generated code
    if not dry_run and user_autoformater:

        # auformat code
        autoformat_code(corrected_files)

    # return changes
    return original_files, corrected_files
