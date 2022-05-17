
from wagon_sync.tag import Tag
from wagon_sync.verb import Verb


class TestTags():

    def test_tag_apply(self):
        """
        verify that the content is correctly transformed
        when a tag is applied to it
        """

        # Arrange
        cha = Verb(
            verb="CHA",
            fill=True)
        tag = Tag(
            verb=cha,
            replacement="pass",
            prefix="# ")

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
                pass# block end
            block after
            """

        # Assert
        assert decorated == expected

        # Cleanup
