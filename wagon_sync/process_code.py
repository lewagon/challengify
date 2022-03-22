
from wagon_common.helpers.file import ensure_path_directory_exists

from wagon_sync.code_edition import replace_content, replace_tag

from wagon_sync.params.delimiters import (
    CHALLENGIFY_VERBS,
    CHALLENGIFY_REPLACEMENTS,
    ITERATE_DELIMITERS,
    CHALLENGE_ONLY_FOR_DELIMITERS)


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
            eat_leading_tabs = configuration.get("eat", False)

            # replace delimiter blocks
            content = replace_content(content, replacement, delimiter_begin, delimiter_end, eat_leading_tabs=eat_leading_tabs)

    return content


def process_versions(content, rule, versions, keep=True):

    # get configurations
    for iterate_verb in CHALLENGIFY_VERBS:

        # skip non delete verbs
        if "fill" in iterate_verb:
            continue

        # retrieve iterate verb params
        verb = iterate_verb["verb"]
        trailing_newlines = iterate_verb["trailing_newlines"] * "\n"

        # retrieve delimiter patterns
        configuration = ITERATE_DELIMITERS[rule]

        version_delimiter_begin = configuration["begin"].replace("verb", verb).replace("__", "_")
        version_delimiter_end = configuration["end"].replace("verb", verb).replace("__", "_") + trailing_newlines

        # iterate through versions
        for version in versions:

            # replace versions in delimiters
            delimiter_begin = version_delimiter_begin.replace("version", version)
            delimiter_end = version_delimiter_end.replace("version", version)

            # handle content
            if keep:

                # clean tag from trailing newlines
                cleaned_delimiter_end = delimiter_end.replace("\n", "")

                # remove delimiters
                content = replace_tag(content, "", delimiter_begin, eat_leading_tabs=True)
                content = replace_tag(content, "", cleaned_delimiter_end, eat_leading_tabs=True)

            else:

                # remove block
                content = replace_content(content, "", delimiter_begin, delimiter_end, eat_leading_tabs=True)

    return content


def process_generators(content, current, other_versions):
    """
    process version only for challengify delimiter generators
    """

    # iterate through patterns to process version generators
    for generator_pattern in CHALLENGE_ONLY_FOR_DELIMITERS.values():

        # replace delimiter generators
        for verb in [d["verb"] for d in CHALLENGIFY_VERBS]:

            # build verb generator and delimiter
            verb_generator = generator_pattern.replace("verb", verb)
            step = "BEGIN" if generator_pattern[-1] == "N" else "END"
            verb_delimiter = f"# ${verb.upper()}_{step}"

            # build generator
            generator = verb_generator.replace("version", current)

            # generate delimiters
            content = content.replace(generator, verb_delimiter)

            # remove generator delimiters for other versions
            for version in other_versions:

                # build generator
                generator = verb_generator.replace("version", version)

                # generate delimiters
                content = replace_tag(content, "", generator, eat_leading_tabs=True)

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
        befores = version_iterator.get_versions_before()
        afters = version_iterator.get_versions_after()
        current = version_iterator.get_version_current()

        # process only to
        content = process_versions(content, "only_to", befores, keep=False)
        content = process_versions(content, "only_to", afters + [current])

        # process only for
        content = process_versions(content, "only_for", befores + afters, keep=False)
        content = process_versions(content, "only_for", [current])

        # process only from
        content = process_versions(content, "only_from", afters, keep=False)
        content = process_versions(content, "only_from", befores + [current])

        # process delimiter generators
        content = process_generators(content, current, befores + afters)

    # write content
    with open(destination, "w") as file:
        file.write(content)
