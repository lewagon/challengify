
from wagon_common.helpers.file import ensure_path_directory_exists

from wagon_sync.params.delimiters import (
    RAW_CODE_DELETE_BEGIN,
    RAW_CODE_DELETE_END,
    RAW_CODE_CHALLENGIFY_BEGIN,
    RAW_CODE_CHALLENGIFY_END,
    LEWAGON_SOLUTION_CODE_DELETE_BEGIN,
    LEWAGON_SOLUTION_CODE_DELETE_END,
    LEWAGON_SOLUTION_CODE_CHALLENGIFY_BEGIN,
    LEWAGON_SOLUTION_CODE_CHALLENGIFY_END,
    LEWAGON_SOLUTION_CODE_REPLACEMENT_PYTHON,
    LEWAGON_SOLUTION_CODE_REPLACEMENT_RUBY,
    # meta delimiters
    META_DELIMITER_VERSION_REPLACEMENT,
    META_DELIMITER_BEFORE_BEGIN,
    META_DELIMITER_BEFORE_END,
    META_DELIMITER_ONLY_BEGIN,
    META_DELIMITER_ONLY_END,
    META_DELIMITER_AFTER_BEGIN,
    META_DELIMITER_AFTER_END,
    ITERATE_IGNORE_CODE_DELETE_BEGIN,
    ITERATE_IGNORE_CODE_DELETE_END,
    ITERATE_IGNORE_CODE_CHALLENGIFY_BEGIN,
    ITERATE_IGNORE_CODE_CHALLENGIFY_END,
)

import re


def process_code(source, destination, file_extension, ignore_run_delimiters=False, version_iterator=None):

    # create destination directory
    ensure_path_directory_exists(destination)

    # read content
    with open(source, "r") as file:
        source_content = file.read()

    # replace challengify run delimiters
    if ignore_run_delimiters:

        # ignore code delete
        source_content = source_content.replace(RAW_CODE_DELETE_BEGIN, ITERATE_IGNORE_CODE_DELETE_BEGIN)
        source_content = source_content.replace(RAW_CODE_DELETE_END, ITERATE_IGNORE_CODE_DELETE_END)

        # ignore code challengify
        source_content = source_content.replace(RAW_CODE_CHALLENGIFY_BEGIN, ITERATE_IGNORE_CODE_CHALLENGIFY_BEGIN)
        source_content = source_content.replace(RAW_CODE_CHALLENGIFY_END, ITERATE_IGNORE_CODE_CHALLENGIFY_END)

    # handle preprocessing for challengify iterate command
    if version_iterator is not None:

        # retrieve current version for delimiters
        challenge_position = version_iterator.iterated_position

        # iterate through meta delimiters
        for delimiter_version in version_iterator.versions:  # iterate through all versions without using the iterator

            # retrieve challenge versions for delimiters
            meta_version_priority = delimiter_version.priority
            meta_version_name = delimiter_version.version

            # build meta version delimiters
            meta_before_begin = META_DELIMITER_BEFORE_BEGIN.replace(META_DELIMITER_VERSION_REPLACEMENT, meta_version_name)
            meta_before_end = META_DELIMITER_BEFORE_END.replace(META_DELIMITER_VERSION_REPLACEMENT, meta_version_name)
            meta_only_begin = META_DELIMITER_ONLY_BEGIN.replace(META_DELIMITER_VERSION_REPLACEMENT, meta_version_name)
            meta_only_end = META_DELIMITER_ONLY_END.replace(META_DELIMITER_VERSION_REPLACEMENT, meta_version_name)
            meta_after_begin = META_DELIMITER_AFTER_BEGIN.replace(META_DELIMITER_VERSION_REPLACEMENT, meta_version_name)
            meta_after_end = META_DELIMITER_AFTER_END.replace(META_DELIMITER_VERSION_REPLACEMENT, meta_version_name)

            # version x removes content with meta delimiters before x and down
            if challenge_position >= meta_version_priority:

                # replace meta delimiters outside of version number by DELETE delimiters (remove content)
                source_content = source_content.replace(meta_before_begin, RAW_CODE_DELETE_BEGIN)
                source_content = source_content.replace(meta_before_end, RAW_CODE_DELETE_END)

            else:

                # remove delimiters inside of version number (keep content)
                source_content = source_content.replace(meta_before_begin, "")
                source_content = source_content.replace(meta_before_end, "")

            # version x removes content with meta delimiters if not equal to x
            if challenge_position != meta_version_priority:

                # replace meta delimiters outside of version number by DELETE delimiters (remove content)
                source_content = source_content.replace(meta_only_begin, RAW_CODE_DELETE_BEGIN)
                source_content = source_content.replace(meta_only_end, RAW_CODE_DELETE_END)

            else:

                # remove delimiters inside of version number (keep content)
                source_content = source_content.replace(meta_only_begin, "")
                source_content = source_content.replace(meta_only_end, "")

            # version x removes content with meta delimiters after x and up
            if challenge_position <= meta_version_priority:

                # replace meta delimiters outside of version number by DELETE delimiters (remove content)
                source_content = source_content.replace(meta_after_begin, RAW_CODE_DELETE_BEGIN)
                source_content = source_content.replace(meta_after_end, RAW_CODE_DELETE_END)

            else:

                # remove delimiters inside of version number (keep content)
                source_content = source_content.replace(meta_after_begin, "")
                source_content = source_content.replace(meta_after_end, "")

    # select replacement string for solution code depending on code language
    if file_extension == "py":
        solution_code_replacement = LEWAGON_SOLUTION_CODE_REPLACEMENT_PYTHON
    else:  # "rb", "sh" or "txt"
        solution_code_replacement = LEWAGON_SOLUTION_CODE_REPLACEMENT_RUBY

    # replace all content within le wagon solution pass delimiters
    # (.|\n)*?                                    non greedily ? capture any characters and new lines (.|\n)*
    # (?<!{LEWAGON_SOLUTION_CODE_CHALLENGIFY_END})       negative lookbehind: assert that what immediately follows is not {LEWAGON_SOLUTION_CODE_CHALLENGIFY_END}
    pattern = f"{LEWAGON_SOLUTION_CODE_CHALLENGIFY_BEGIN}(.|\n)*?(?<!{LEWAGON_SOLUTION_CODE_CHALLENGIFY_END}){LEWAGON_SOLUTION_CODE_CHALLENGIFY_END}"
    replaced_content = re.sub(pattern, solution_code_replacement, source_content)

    # remove all content within le wagon solution delete delimiters
    pattern = f"{LEWAGON_SOLUTION_CODE_DELETE_BEGIN}(.|\n)*?(?<!{LEWAGON_SOLUTION_CODE_DELETE_END}){LEWAGON_SOLUTION_CODE_DELETE_END}"
    replaced_content = re.sub(pattern, "", replaced_content)

    # replace back challengify run delimiters
    if ignore_run_delimiters:

        # ignore code delete
        replaced_content = replaced_content.replace(ITERATE_IGNORE_CODE_DELETE_BEGIN, RAW_CODE_DELETE_BEGIN)
        replaced_content = replaced_content.replace(ITERATE_IGNORE_CODE_DELETE_END, RAW_CODE_DELETE_END)

        # ignore code challengify
        replaced_content = replaced_content.replace(ITERATE_IGNORE_CODE_CHALLENGIFY_BEGIN, RAW_CODE_CHALLENGIFY_BEGIN)
        replaced_content = replaced_content.replace(ITERATE_IGNORE_CODE_CHALLENGIFY_END, RAW_CODE_CHALLENGIFY_END)

    # write content
    with open(destination, "w") as file:
        file.write(replaced_content)
