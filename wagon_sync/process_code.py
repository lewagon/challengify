
from wagon_common.helpers.file import ensure_path_directory_exists

from wagon_sync.code_edition import replace_content

from wagon_sync.params.delimiters import (
    CHALLENGIFY_DELIMITERS,
    CHALLENGIFY_REPLACEMENTS,
    # meta delimiters
    META_DELIMITER_VERSION_REPLACEMENT,
    META_DELIMITER_BEFORE_BEGIN,
    META_DELIMITER_BEFORE_END,
    META_DELIMITER_ONLY_BEGIN,
    META_DELIMITER_ONLY_END,
    META_DELIMITER_AFTER_BEGIN,
    META_DELIMITER_AFTER_END,
)


def process_delimiters(content, file_extension, verb_delimiters):

    # iterate through delimiter verbs
    for verb, configurations in verb_delimiters.items():

        # retrieve verb replacements
        replacements = CHALLENGIFY_REPLACEMENTS[verb]

        # select replacement string
        if file_extension in replacements:
            replacement = replacements[file_extension]
        else:
            replacement = replacements["default"]

        # iterate through delimiter configurations
        for configuration in configurations:

            # retrieve configuration delimiters
            delimiter_begin = configuration["begin"]
            delimiter_end = configuration["end"]

            # replace delimiter blocks
            content = replace_content(content, replacement, delimiter_begin, delimiter_end)

    return content


def process_code(source, destination, file_extension, version_iterator=None):

    # create destination directory
    ensure_path_directory_exists(destination)

    # read content
    with open(source, "r") as file:
        source_content = file.read()

    # run challengify
    if version_iterator is None:

        # process content through challengify delimiters
        replaced_content = process_delimiters(source_content, file_extension, CHALLENGIFY_DELIMITERS)

    # run challengify iterate
    else:

        # retrieve current version for delimiters
        challenge_position = version_iterator.iterated_position

        # iterate through meta delimiters
        for delimiter_version in version_iterator.versions:  # iterate through all versions without using the iterator

            # retrieve challenge versions for delimiters
            meta_version_position = delimiter_version.position
            meta_version_name = delimiter_version.version

            # build meta version delimiters
            meta_before_begin = META_DELIMITER_BEFORE_BEGIN.replace(META_DELIMITER_VERSION_REPLACEMENT, meta_version_name)
            meta_before_end = META_DELIMITER_BEFORE_END.replace(META_DELIMITER_VERSION_REPLACEMENT, meta_version_name)
            meta_only_begin = META_DELIMITER_ONLY_BEGIN.replace(META_DELIMITER_VERSION_REPLACEMENT, meta_version_name)
            meta_only_end = META_DELIMITER_ONLY_END.replace(META_DELIMITER_VERSION_REPLACEMENT, meta_version_name)
            meta_after_begin = META_DELIMITER_AFTER_BEGIN.replace(META_DELIMITER_VERSION_REPLACEMENT, meta_version_name)
            meta_after_end = META_DELIMITER_AFTER_END.replace(META_DELIMITER_VERSION_REPLACEMENT, meta_version_name)

            # version x removes content with meta delimiters before x and down
            if challenge_position >= meta_version_position:

                # replace meta delimiters outside of version number by DELETE delimiters (remove content)
                source_content = source_content.replace(meta_before_begin, RAW_CODE_DELETE_BEGIN)
                source_content = source_content.replace(meta_before_end, RAW_CODE_DELETE_END)

            else:

                # remove delimiters inside of version number (keep content)
                source_content = source_content.replace(meta_before_begin, "")
                source_content = source_content.replace(meta_before_end, "")

            # version x removes content with meta delimiters if not equal to x
            if challenge_position != meta_version_position:

                # replace meta delimiters outside of version number by DELETE delimiters (remove content)
                source_content = source_content.replace(meta_only_begin, RAW_CODE_DELETE_BEGIN)
                source_content = source_content.replace(meta_only_end, RAW_CODE_DELETE_END)

            else:

                # remove delimiters inside of version number (keep content)
                source_content = source_content.replace(meta_only_begin, "")
                source_content = source_content.replace(meta_only_end, "")

            # version x removes content with meta delimiters after x and up
            if challenge_position <= meta_version_position:

                # replace meta delimiters outside of version number by DELETE delimiters (remove content)
                source_content = source_content.replace(meta_after_begin, RAW_CODE_DELETE_BEGIN)
                source_content = source_content.replace(meta_after_end, RAW_CODE_DELETE_END)

            else:

                # remove delimiters inside of version number (keep content)
                source_content = source_content.replace(meta_after_begin, "")
                source_content = source_content.replace(meta_after_end, "")

    # write content
    with open(destination, "w") as file:
        file.write(replaced_content)
