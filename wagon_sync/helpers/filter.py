"""
re helper
"""

import re


def list_files_matching_dirs(file_list, directory_path_list):
    """
    returns a list of files matching at least one of the provided path
    """

    # return an empty list if no rules are provided
    if len(directory_path_list) == 0:
        return []

    # build file list and patterns
    all_files = "\n".join(file_list)
    all_patterns = "^" + ".*|^".join(directory_path_list) + ".*"

    # find all files matching at least one of the provided path
    excluded_files = re.findall(all_patterns, all_files, re.M)  # multiline re

    return sorted(excluded_files)


def list_files_matching_pattern(file_list, pattern_list):
    """
    returns a list of files matching at least one of the provided pattern
    """

    # return an empty list if no rules are provided
    if len(pattern_list) == 0:
        return []

    # build file list and patterns
    all_files = "\n".join(file_list)
    all_patterns = ".*" + ".*|.*".join(pattern_list) + ".*"

    # find all files matching at least one of the provided path
    excluded_files = re.findall(all_patterns, all_files, re.M)  # multiline re

    return sorted(excluded_files)
