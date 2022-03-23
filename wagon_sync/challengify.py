
from wagon_sync.file_scope import FileScope

from wagon_sync.language_decorators import LanguageDecorators


class Challengify:

    def __init__(self):

        self.decorators = LanguageDecorators()

    def process(self, file_scope: FileScope):
        """
        challengify run
        """

        # iterate through files
        for file in file_scope:

            # retrieve file language decorator
            decorator = self.decorators.get(file.language)

            # apply decorator
            file.decorate(decorator)

    def iterate(self, file_scope: FileScope):
        """
        challengify iterate
        """

        pass
