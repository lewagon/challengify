
from wagon_sync.verbs import Verbs
from wagon_sync.verb import Verb
from wagon_sync.tag import Tag

from wagon_sync.params.delimiters import (
    DELIMITER_PREFIX,
    DELIMITER_SUFFIX_BEGIN,
    DELIMITER_SUFFIX_END,
    CHALLENGIFY_REPLACEMENTS)

from colorama import Fore, Style


class Decorator:

    def __init__(self, verbs: Verbs, language, prefix, suffix=None):

        self.language = language
        self.prefix = prefix
        self.suffix = suffix

        self.replacement = CHALLENGIFY_REPLACEMENTS.get(language, CHALLENGIFY_REPLACEMENTS["default"])

        self.verbs = verbs
        self.tags = self.build_tags()

    def decorate(self, content):

        decorated = content

        # iterate through tags
        for tag in self.tags:

            decorated = tag.apply(decorated)

        return decorated

    def build_tags(self):

        tags = []

        # iterate through verbs
        for verb in self.verbs.all:

            replacement = self.replacement if verb.fill else ""

            tag = Tag(
                begin=self.begin_delimiter(verb),
                end=self.end_delimiter(verb),
                replacement=replacement,
                eat_indentation=verb.eat_indentation)

            tags.append(tag)

        return tags

    def begin_delimiter(self, verb: Verb):

        return self.build_delimiter(verb, DELIMITER_SUFFIX_BEGIN)

    def end_delimiter(self, verb: Verb):

        return self.build_delimiter(verb, DELIMITER_SUFFIX_END)

    def build_delimiter(self, verb: Verb, suffix):

        decorated_verb = (
            self.prefix
            + DELIMITER_PREFIX
            + verb.name
            + suffix)

        if self.suffix is not None:
            decorated_verb += self.suffix

        decorated_verb += verb.trailing_newlines * "\n"

        return decorated_verb

    def print(self):

        cha = self.verbs.all[0]

        print(Fore.BLUE
              + f"\nDecorator {self.language}:"
              + Style.RESET_ALL
              + f"\n- prefix: `{self.prefix}`"
              + (f"\n- suffix: `{self.suffix}`" if self.suffix else "")
              + f"\n- {cha.name} begin: {self.begin_delimiter(cha)}"
              + f"\n- {cha.name} end: {self.end_delimiter(cha)}")

    def print_tags(self):

        print(Fore.BLUE
              + f"\nDecorator {self.language}:"
              + Style.RESET_ALL)
        [t.print() for t in self.tags]
