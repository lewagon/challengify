
from wagon_sync.verbs import Verbs


class TestVerbs():

    def test_print_verbs(self):
        """
        visual test (use `pytest -s`)
        """

        # Arrange
        verbs = Verbs()

        # Act

        # Assert
        verbs.print()

        assert True

        # Cleanup
