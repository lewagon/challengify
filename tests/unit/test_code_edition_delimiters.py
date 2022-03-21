
from wagon_sync.delimiters import Delimiters


class TestCodeEditionDelimiters():

    def test_delimiters_are_unique(self):
        """
        test that delimiters are unique
        in order to prevent delimiter blocks to partially consume one another
        """
        # Arrange

        # Act
        delimiters = Delimiters().all

        # iterate through languages
        for language, delimiter in delimiters.items():

            # iterate through verbs
            elements = [v for t in delimiter.tags() for v in [t.begin, t.end]]

            delimiter.print_tags()

            # Assert
            assert len(elements) == len(set(elements))

        # Cleanup
