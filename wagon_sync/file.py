
from wagon_sync.language_decorators import LanguageDecorators
from wagon_sync.decorator import Decorator

import re


class File:

    # TODO refacto
    cached_content = {}
    cached_delimiters = {}

    # TODO refacto
    decorators = LanguageDecorators()

    def __init__(self, source, destination, language):

        self.source = source
        self.destination = destination
        self.language = language

        self.content = self.__load(self.source)

        self.decorator = self.decorators.get(self.language)

        self.delimiters = self.__load_delimiters(self.content)

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

    def __load_delimiters(self, content):
        """
        scan file for delimiters
        """

        delimiters = []

        # TODO
        # self.decorator.tag_pattern

        # load cached delimiters
        if self.source in self.cached_delimiters:
            return self.cached_delimiters[self.source]

        # search for delimiters
        matches = re.search("(# \\$.*_BEGIN)|(# \\$.*_END)", content)

        delimiters = bool(matches)

        # cache delimiters
        self.cached_delimiters[self.source] = delimiters

        return delimiters

    def decorate(self, decorator: Decorator):

        # decorate content
        if self.delimiters:
            self.decorated = decorator.decorate(self.content)
        else:
            self.decorated = self.content

        # write destination
        with open(self.destination, "w") as file:
            file.write(self.decorated)
