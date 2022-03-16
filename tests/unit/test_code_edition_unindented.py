
from wagon_sync.code_edition import replace_content


class TestUnindentedCodeEdition():

    def test_unindented_suppression(self):
        """
        test that a newline appears between the content
        when an unindented block of content is removed
        without the use of any dedicated separators
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

after
        """

        # Act
        replaced_content = replace_content(source, replacement, begin, end)

        # Assert
        assert replaced_content == expected_result

        # Cleanup

    def test_unindented_extra_line_suppression(self):
        """
        test that no newlines appear between the content
        when an unindented block of content is removed
        using a single newline consuming dedicated end separator
        """
        # Arrange
        source = """
before
$BEGIN
content
$END_LINE
after
        """
        replacement = ""
        begin = "$BEGIN"
        end = "$END_LINE\n"

        expected_result = """
before
after
        """

        # Act
        replaced_content = replace_content(source, replacement, begin, end)

        # Assert
        assert replaced_content == expected_result

        # Cleanup

    def test_unindented_no_line_suppression(self):
        """
        test that all newlines are preserved between the content
        when an unindented block of content is removed
        without the use of any dedicated separators
        """
        # Arrange
        source = """
before

$BEGIN
content
$END_LINES

after
        """
        replacement = ""
        begin = "$BEGIN"
        end = "$END_LINES"

        expected_result = """
before



after
        """

        # Act
        replaced_content = replace_content(source, replacement, begin, end)

        # Assert
        assert replaced_content == expected_result

        # Cleanup

    def test_unindented_extra_lines_suppression(self):
        """
        test that a single newline is preserved between the content
        when an unindented block of content is removed
        using a double newline consuming dedicated end separator
        """
        # Arrange
        source = """
before

$BEGIN
content
$END_LINES

after
        """
        replacement = ""
        begin = "$BEGIN"
        end = "$END_LINES\n\n"

        expected_result = """
before

after
        """

        # Act
        replaced_content = replace_content(source, replacement, begin, end)

        # Assert
        assert replaced_content == expected_result

        # Cleanup

    def test_unindented_all_lines_suppression(self):
        """
        test that no newlines appear between the content
        when an unindented block of content is removed
        using newline consuming dedicated begin and end separators
        """
        # Arrange
        source = """
before

$BEGIN
content
$END_LINES

after
        """
        replacement = ""
        begin = "\n$BEGIN"
        end = "$END_LINES\n\n"

        expected_result = """
before
after
        """

        # Act
        replaced_content = replace_content(source, replacement, begin, end)

        # Assert
        assert replaced_content == expected_result

        # Cleanup
