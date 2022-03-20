
from wagon_sync.code_edition import replace_content


class TestCodeSuppressionUnindented():

    def test_unindented_delete(self):
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

    def test_unindented_spaced_delete(self):
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

    def test_unindented_erase(self):
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
        replaced_content = replace_content(source, replacement, begin, end, eat_leading_tabs=True)

        # Assert
        assert replaced_content == expected_result

        # Cleanup

    def test_unindented_wipe(self):
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
$END

after
        """
        replacement = ""
        begin = "$BEGIN"
        end = "$END\n"

        expected_result = """
before

after
        """

        # Act
        replaced_content = replace_content(source, replacement, begin, end, eat_leading_tabs=True)

        # Assert
        assert replaced_content == expected_result

        # Cleanup

    def test_unindented_implode(self):
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
$END

after
        """
        replacement = ""
        begin = "$BEGIN"
        end = "$END\n\n"

        expected_result = """
before
after
        """

        # Act
        replaced_content = replace_content(source, replacement, begin, end, eat_leading_tabs=True)

        # Assert
        assert replaced_content == expected_result

        # Cleanup
