
from wagon_sync.verb import Verb
from wagon_sync.verbs import Verbs
from wagon_sync.tag import Tag

from wagon_sync.params.delimiters import (
    DELIMITER_PREFIX,
    DELIMITER_SUFFIX_BEGIN,
    DELIMITER_SUFFIX_END)

from colorama import Fore, Style


class Delimiter:

    def __init__(self, language, prefix, suffix=None, composed=False):

        self.language = language
        self.prefix = prefix
        self.suffix = suffix

        # TODO: use a singleton / metaclass decorator
        self.verbs = Verbs()

    def tags(self):

        tags = []

        # iterate through verbs
        for verb in self.verbs.all:

            tag = Tag(
                begin=self.begin_tag(verb),
                end=self.end_tag(verb),
                fill=verb.fill,
                eat_indentation=verb.eat_indentation)

            tags.append(tag)

        return tags

    def begin_tag(self, verb: Verb):

        return self.decorate_verb(verb, DELIMITER_SUFFIX_BEGIN)

    def end_tag(self, verb: Verb):

        return self.decorate_verb(verb, DELIMITER_SUFFIX_END)

    def decorate_verb(self, verb: Verb, suffix):

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
              + f"\nDelimiter {self.language}:"
              + Style.RESET_ALL
              + f"\n- prefix: `{self.prefix}`"
              + (f"\n- suffix: `{self.suffix}`" if self.suffix else "")
              + f"\n- cha begin: {self.begin_tag(cha)}"
              + f"\n- cha end: {self.end_tag(cha)}")

    def print_tags(self):

        print(Fore.BLUE
              + f"\nDelimiter {self.language}:"
              + Style.RESET_ALL)
        [t.print() for t in self.tags()]
