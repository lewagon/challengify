
from wagon_sync.verbs import Verbs
from wagon_sync.tag import Tag

from wagon_sync.params.delimiters import (
    REPLACEMENT_CONTENT,
    CUSTOM_REPLACEMENTS)

from colorama import Fore, Style


class Decorator:

    def __init__(self, verbs: Verbs, language, prefix, suffix=None):

        self.language = language
        self.prefix = prefix
        self.suffix = suffix

        # build replacement
        if language in CUSTOM_REPLACEMENTS:
            self.replacement = CUSTOM_REPLACEMENTS[language]
        else:
            self.replacement = f"{self.prefix}{REPLACEMENT_CONTENT}{self.suffix if self.suffix is not None else ''}"

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

            tag = Tag(verb, replacement, self.prefix, self.suffix)

            tags.append(tag)

        return tags

    def print(self):

        cha = self.tags[0]

        print(Fore.BLUE
              + f"\nDecorator {self.language}:"
              + Style.RESET_ALL
              + f"\n- prefix: `{self.prefix}`"
              + (f"\n- suffix: `{self.suffix}`" if self.suffix else "")
              + f"\n- {cha.verb.name} begin: {cha.begin}"
              + f"\n- {cha.verb.name} end: {cha.end}")

    def print_tags(self):

        print(Fore.BLUE
              + f"\nDecorator {self.language}:"
              + Style.RESET_ALL)
        [t.print() for t in self.tags]
