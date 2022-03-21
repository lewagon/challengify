
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

    def decorate_verb(self, verb, suffix):

        decorated_verb = (
            self.prefix
            + DELIMITER_PREFIX
            + verb
            + suffix)

        if self.suffix is not None:
            decorated_verb += self.suffix

        return decorated_verb

    def begin_tag(self, verb):

        return self.decorate_verb(verb, DELIMITER_SUFFIX_BEGIN)

    def end_tag(self, verb):

        return self.decorate_verb(verb, DELIMITER_SUFFIX_END)

    def print(self):

        print(Fore.BLUE
              + f"\nDelimiter {self.language}:"
              + Style.RESET_ALL
              + f"\n- prefix: `{self.prefix}`"
              + (f"\n- suffix: `{self.suffix}`" if self.suffix else "")
              + f"\n- cha begin: {self.begin_tag('CHA')}"
              + f"\n- cha end: {self.end_tag('CHA')}")
