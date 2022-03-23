
from wagon_sync.file import File
from wagon_sync.challengify import Challengify

import os


class TestChallengify():

    def test_print_language_decorators(self):

        # Arrange
        source_file_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "code",
            "python",
            "code.py")
        source_file = File(source_file_path, "/dev/null", "py")

        destination_file_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "code",
            "python",
            "code_generated.py")
        destination_file = File(destination_file_path, "/dev/null", "py")

        challengify = Challengify()

        # Act

        challengify.process([source_file])

        # Assert
        assert source_file.decorated == destination_file.content

        # Cleanup
