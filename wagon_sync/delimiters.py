
from wagon_sync.params.delimiters import LANGUAGE_INLINE_COMMENT_DELIMITERS

from wagon_sync.delimiter import Delimiter


class Delimiters:

    def __init__(self):

        self.delimiters = {}

        # store delimiters
        for language, params in LANGUAGE_INLINE_COMMENT_DELIMITERS.items():

            delimiter = Delimiter(language=language, **params)

            self.delimiters[language] = delimiter

    def print(self):

        # print delimiters
        [d.print() for d in self.delimiters.values()]
