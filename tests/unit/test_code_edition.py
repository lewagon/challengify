
from wagon_sync.code_edition import replace_content


class TestCodeEdition():

    def test_replacement(self):
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

    def test_suppression(self):
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

after
        """

        # Act
        replaced_content = replace_content(source, replacement, begin, end)

        # Assert
        assert replaced_content == expected_result

        # Cleanup

    def test_indented_suppression(self):
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
