
from wagon_sync.code_edition import replace_content


class TestCodeEditionReplacement():

    def test_replacement(self):
        """
        test inline unindented code replacement
        """
        # Arrange
        source = """
            before
            $BEGIN
            content
            $END
            after
        """
        replacement = "pass"
        begin = "$BEGIN"
        end = "$END"

        expected_result = """
            before
            pass
            after
        """

        # Act
        replaced_content = replace_content(source, replacement, begin, end)

        # Assert
        assert replaced_content == expected_result

        # Cleanup

    def test_indented_replacement(self):
        """
        test inline indented code replacement
        """
        # Arrange
        source = """
            before
                $BEGIN
                content
                $END
            after
        """
        replacement = "pass"
        begin = "$BEGIN"
        end = "$END"

        expected_result = """
            before
                pass
            after
        """

        # Act
        replaced_content = replace_content(source, replacement, begin, end)

        # Assert
        assert replaced_content == expected_result

        # Cleanup
