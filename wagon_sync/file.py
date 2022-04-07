
from wagon_sync.decorator import Decorator


class File:

    cached_content = {}

    def __init__(self, source, destination, language):

        self.source = source
        self.destination = destination
        self.language = language

        self.content = self.__load(self.source)

    def __load(self, source):
        """
        cached file loader
        """

        # load cached content
        if source in self.cached_content:
            return self.cached_content[source]

        # read source
        with open(source, 'r') as file:
            content = file.read()

        # cache content
        self.cached_content[source] = content

        return content

    def decorate(self, decorator: Decorator):

        # decorate content
        self.decorated = decorator.decorate(self.content)

        # write destination
        with open(self.destination, "w") as file:
            file.write(self.decorated)
