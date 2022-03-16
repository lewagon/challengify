
from wagon_common.helpers.file import ensure_path_directory_exists

from wagon_sync.code_edition import replace_content

from wagon_sync.params.delimiters import (
    CHALLENGIFY_DELIMITERS,
    CHALLENGIFY_REPLACEMENTS,
    ITERATE_DELIMITERS)


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


def process_versions(content, rule, versions, keep=True):

    # retrieve delimiter patterns
    version_delimiter_begin = ITERATE_DELIMITERS[rule]["begin"]
    version_delimiter_end = ITERATE_DELIMITERS[rule]["end"]

    # iterate through versions
    for version in versions:

        # replace versions in delimiters
        delimiter_begin = version_delimiter_begin.replace("version", version)
        delimiter_end = version_delimiter_end.replace("version", version)

        # handle content
        if keep:

            # remove delimiters
            content = content.replace(delimiter_begin, "")
            content = content.replace(delimiter_end, "")

        else:

            # remove block
            content = replace_content(content, "", delimiter_begin, delimiter_end)

    return content


def process_code(source, destination, file_extension, version_iterator=None):

    # create destination directory
    ensure_path_directory_exists(destination)

    # read content
    with open(source, "r") as file:
        content = file.read()

    # run challengify
    if version_iterator is None:

        # process content through challengify delimiters
        content = process_delimiters(content, file_extension, CHALLENGIFY_DELIMITERS)

    # run challengify iterate
    else:

        # retrieve versions
        versions_before_current = version_iterator.get_versions_before()
        versions_after_current = version_iterator.get_versions_after()
        version_current = version_iterator.get_version_current()

        # process only to
        content = process_versions(content, "only_to", versions_before_current, keep=False)
        content = process_versions(content, "only_to", versions_after_current + [version_current])

        # process only for
        content = process_versions(content, "only_for", versions_before_current + versions_after_current, keep=False)
        content = process_versions(content, "only_for", [version_current])

        # process only from
        content = process_versions(content, "only_from", versions_after_current, keep=False)
        content = process_versions(content, "only_from", versions_before_current + [version_current])

    # write content
    with open(destination, "w") as file:
        file.write(content)
