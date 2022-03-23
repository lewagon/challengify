
from wagon_sync.decorator import Decorator


class File:

    def __init__(self, source, destination, language):

        self.source = source
        self.destination = destination
        self.language = language

        # read source
        with open(self.source, 'r') as file:
            self.content = file.read()

    def decorate(self, decorator: Decorator):

        # decorate content
        self.decorated = decorator.decorate(self.content)

        # write destination
        with open(self.destination, "w") as file:
            file.write(self.decorated)
