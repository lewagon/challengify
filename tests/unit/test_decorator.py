
from wagon_sync.verbs import Verbs
from wagon_sync.decorator import Decorator


class TestDecorator():

    def test_decorate(self):
        """
        verify that the content is correctly transformed
        when the decorated is applied to it
        """

        # Arrange
        verbs = Verbs()
        python_decorator = Decorator(verbs, "py", "# ", None)

        # Act
        decorated = python_decorator.decorate("""
            block before
                # $CHA_BEGIN
                some content inside
                # $CHA_END# block end
                # $ERASE_BEGIN
                some content inside
                # $ERASE_END
            block after
            """)

        expected = """
            block before
                pass  # YOUR CODE HERE# block end
            block after
            """

        # Assert
        assert decorated == expected

        # Cleanup
