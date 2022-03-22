
from wagon_sync.language_decorators import LanguageDecorators


class TestLanguageDecorators():

    def test_print_language_decorators(self):
        """
        visual test (use `pytest -s`)
        """

        # Arrange
        language_decorators = LanguageDecorators()

        # Act

        # Assert
        language_decorators.print()
        list(language_decorators.all.values())[0].print_tags()

        assert True

        # Cleanup

    def test_language_delimiters_are_unique(self):
        """
        test that language_decorators are unique
        in order to prevent decorator blocks to partially consume one another
        """
        # Arrange

        # Act
        language_decorators = LanguageDecorators().all

        # iterate through languages
        for language, decorator in language_decorators.items():

            # iterate through verbs
            elements = [v for t in decorator.tags for v in [t.begin, t.end]]

            decorator.print_tags()

            # Assert
            assert len(elements) == len(set(elements))

        # Cleanup
