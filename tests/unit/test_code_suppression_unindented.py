
from wagon_sync.code_edition import replace_content


class TestCodeSuppressionIndented():

    def test_indented_delete(self):
        """
        test that indented suppression
        leaves in place a blank line with undesired indentation
        """
        # Arrange
        source = """
            before
                $BEGIN
                content
                $END
            after
        """
        replacement = ""
        begin = "$BEGIN"
        end = "$END"

        expected_result = """
            before
""" + "                " + """
            after
        """

        # Act
        replaced_content = replace_content(source, replacement, begin, end)

        # Assert
        assert replaced_content == expected_result

        # Cleanup
