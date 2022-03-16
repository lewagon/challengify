
from wagon_sync.code_edition import replace_content


class TestCodeEdition():

    def test_delimiters_replacement(self):
        """
        # test that exec count integers are present when no action is performed
        """
        # Arrange
        source = """
            before
            $BEGIN
            content
            $END
            after
        """
        replacement = "replacement"
        begin = "$BEGIN"
        end = "$END"

        expected_result = """
            before
            replacement
            after
        """

        # Act
        replaced_content = replace_content(source, replacement, begin, end)

        # Assert
        assert replaced_content == expected_result

        # Cleanup
