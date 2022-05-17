
from wagon_sync.params.delimiters import CHALLENGIFY_VERBS

from wagon_sync.verb import Verb


class Verbs:

    def __init__(self):

        # store verbs
        self.all = [Verb(**params) for params in CHALLENGIFY_VERBS]

    def print(self):

        # print delimiters
        [v.print() for v in self.all]
