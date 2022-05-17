
from wagon_sync.language_decorators import LanguageDecorators
from wagon_sync.decorator import Decorator

import re


from wagon_sync.code_edition import replace_content, replace_tag

from wagon_sync.params.delimiters import (
    CHALLENGIFY_VERBS,
    ITERATE_VERSION_DELIMITERS,
    ITERATE_VERSION_META_DELIMITERS)


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
        configuration = ITERATE_VERSION_DELIMITERS[rule]

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
    for generator_pattern in ITERATE_VERSION_META_DELIMITERS.values():

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


class File:

    # TODO refacto
    cached_content = {}
    cached_delimiters = {}

    # TODO refacto
    decorators = LanguageDecorators()

    def __init__(self, source, destination, language):

        self.source = source
        self.destination = destination
        self.language = language

        self.content = self.__load(self.source)

        self.decorator = self.decorators.get(self.language)

        self.delimiters = self.__load_delimiters(self.content)

    def __load(self, source):
        """
        cached file loader
        """

        # load cached content
        if source in self.cached_content:
            return self.cached_content[source]

        # read source
        with open(source, 'r') as file:
            content = file.read()

        # cache content
        self.cached_content[source] = content

        return content

    def __load_delimiters(self, content):
        """
        scan file for delimiters
        """

        # TODO parse other languages
        # if self.language not in ["py", "rb", "sh", "txt", "md", "ipynb"]:
        if self.language not in ["py", "rb", "sh", "txt", "ipynb"]:
            return True

        delimiters = []

        # TODO
        # self.decorator.tag_pattern

        # load cached delimiters
        if self.source in self.cached_delimiters:
            return self.cached_delimiters[self.source]

        # search for delimiters
        matches = re.search("(# \\$.*_BEGIN)|(# \\$.*_END)", content)

        delimiters = bool(matches)

        # cache delimiters
        self.cached_delimiters[self.source] = delimiters

        return delimiters

    def decorate(self, decorator: Decorator):

        # decorate content
        if self.delimiters:
            self.decorated = decorator.decorate(self.content)
        else:
            self.decorated = self.content

        # write destination
        with open(self.destination, "w") as file:
            file.write(self.decorated)

    def challengify_iterate(self, version_iterator):

        content = self.content

        # retrieve versions
        befores = version_iterator.get_versions_before()
        afters = version_iterator.get_versions_after()
        current = version_iterator.get_version_current()

        # process version macro
        content = content.replace(self.decorator.version_macro, current)
        content = content.replace(self.decorator.position_macro, str(version_iterator.position(current)))

        if self.delimiters:

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
        with open(self.destination, "w") as file:
            file.write(content)
