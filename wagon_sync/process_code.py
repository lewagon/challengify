
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


def process_code(source, destination, file_extension, ignore_run_delimiters, version_pre_clean=None):

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
    if version_pre_clean is not None:

        # retrieve min, max and current version for delimiters
        min_version, max_version, version = version_pre_clean

        # iterate through meta delimiters
        for meta_version in range(min_version, max_version + 1):

            # build meta version delimiters
            meta_before_begin = META_DELIMITER_BEFORE_BEGIN.replace(META_DELIMITER_VERSION_REPLACEMENT, str(meta_version))
            meta_before_end = META_DELIMITER_BEFORE_END.replace(META_DELIMITER_VERSION_REPLACEMENT, str(meta_version))
            meta_only_begin = META_DELIMITER_ONLY_BEGIN.replace(META_DELIMITER_VERSION_REPLACEMENT, str(meta_version))
            meta_only_end = META_DELIMITER_ONLY_END.replace(META_DELIMITER_VERSION_REPLACEMENT, str(meta_version))
            meta_after_begin = META_DELIMITER_AFTER_BEGIN.replace(META_DELIMITER_VERSION_REPLACEMENT, str(meta_version))
            meta_after_end = META_DELIMITER_AFTER_END.replace(META_DELIMITER_VERSION_REPLACEMENT, str(meta_version))

            # version x removes content with meta delimiters before x and down
            if version >= meta_version:

                # replace meta delimiters outside of version number by DELETE delimiters (remove content)
                source_content = source_content.replace(meta_before_begin, RAW_CODE_DELETE_BEGIN)
                source_content = source_content.replace(meta_before_end, RAW_CODE_DELETE_END)

            else:

                # remove delimiters inside of version number (keep content)
                source_content = source_content.replace(meta_before_begin, "")
                source_content = source_content.replace(meta_before_end, "")

            # version x removes content with meta delimiters if not equal to x
            if version != meta_version:

                # replace meta delimiters outside of version number by DELETE delimiters (remove content)
                source_content = source_content.replace(meta_only_begin, RAW_CODE_DELETE_BEGIN)
                source_content = source_content.replace(meta_only_end, RAW_CODE_DELETE_END)

            else:

                # remove delimiters inside of version number (keep content)
                source_content = source_content.replace(meta_only_begin, "")
                source_content = source_content.replace(meta_only_end, "")

            # version x removes content with meta delimiters after x and up
            if version <= meta_version:

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
    else:  # "rb" or "sh"
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
