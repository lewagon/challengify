
from wagon_sync.params.delimiters import CHALLENGIFY_DELIMITERS


class TestCodeEditionDelimiters():

    def test_delimiters_are_unique(self):
        """
        test that delimiters are unique
        in order to prevent delimiter blocks to partially consume one another
        """
        # Arrange

        # Act
        delimiters = CHALLENGIFY_DELIMITERS.values()
        elements = [v for l in delimiters for d in l for v in d.values()]

        # Assert
        assert len(elements) == len(set(elements))

        # Cleanup
