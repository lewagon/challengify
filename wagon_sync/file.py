
from wagon_sync.decorator import Decorator


class File:

    def __init__(self, path, language):

        self.path = path
        self.language = language

        # read file content
        with open(self.path, 'r') as file:
            self.content = file.read()

    def decorate(self, decorator: Decorator):

        # TODO - rewrite this whole method without the self.*

        # decorate content
        self.decorated = decorator.decorate(self.content)

        # write destination file
        self.decorated  # TODO - only for tests / rewrite test_challengify accordingly
