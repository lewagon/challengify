
from wagon_sync.verb import Verb

from wagon_sync.params.delimiters import (
    DELIMITER_PREFIX,
    DELIMITER_SUFFIX_BEGIN,
    DELIMITER_SUFFIX_END)
from wagon_sync.code_edition import replace_content


class Tag:  # Mask

    def __init__(self, verb: Verb, replacement, prefix, suffix=None):

        self.verb = verb
        self.prefix = prefix
        self.suffix = suffix

        self.begin = self.begin_delimiter(verb)   # begin delimiter
        self.end = self.end_delimiter(verb)       # end delimiter
        self.replacement = replacement
        self.eat_indentation = verb.eat_indentation

    def apply(self, content):

        decorated = replace_content(
            content, self.replacement, self.begin, self.end, self.eat_indentation)

        return decorated

    def begin_delimiter(self, verb: Verb):

        return self.build_delimiter(verb, DELIMITER_SUFFIX_BEGIN)

    def end_delimiter(self, verb: Verb):

        return self.build_delimiter(verb, DELIMITER_SUFFIX_END, end=True)

    def build_delimiter(self, verb: Verb, suffix, end=False):

        decorated_verb = (
            self.prefix
            + DELIMITER_PREFIX
            + verb.name
            + suffix)

        if self.suffix is not None:
            decorated_verb += self.suffix

        decorated_verb += verb.trailing_newlines * "\n" if end else ""

        return decorated_verb

    def print(self):

        begin = self.begin.replace("\n", "\\n")
        end = self.end.replace("\n", "\\n")

        print(f"\n- begin: {begin}"
              + f"\n- end: {end}"
              + f"\n- replacement: {self.replacement}"
              + f"\n- eat_indentation: {self.eat_indentation}")
