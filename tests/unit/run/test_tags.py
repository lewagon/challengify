
from wagon_sync.tag import Tag


class TestTags():

    def test_tag_apply(self):
        """
        verify that the content is correctly transformed
        when a tag is applied to it
        """

        # Arrange
        tag = Tag(
            begin="# $CHA_BEGIN",
            end="# $CHA_END",
            replacement="# pass",
            eat_indentation=False)

        # Act
        decorated = tag.apply("""
            block before
                # $CHA_BEGIN
                some content inside
                # $CHA_END# block end
            block after
            """)

        expected = """
            block before
                # pass# block end
            block after
            """

        # Assert
        assert decorated == expected

        # Cleanup
