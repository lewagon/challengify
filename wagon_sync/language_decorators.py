
from wagon_sync.params.delimiters import LANGUAGE_INLINE_COMMENT_DELIMITERS

from wagon_sync.verbs import Verbs
from wagon_sync.decorator import Decorator


class LanguageDecorators:

    def __init__(self):

        # TODO: use a singleton / metaclass decorator
        self.verbs = Verbs()

        self.all = {}

        # store decorators
        for language, params in LANGUAGE_INLINE_COMMENT_DELIMITERS.items():

            decorator = Decorator(language=language, verbs=self.verbs, **params)

            self.all[language] = decorator

    def get(self, language):

        return self.all[language]

    def print(self):

        # print decorators
        [d.print() for d in self.all.values()]
