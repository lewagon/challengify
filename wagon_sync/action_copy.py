
from wagon_common.helpers.file import cp

import os


def action_copy(source, destination, command_destination):

    # build destination path
    destination_path = os.path.join(
        command_destination,
        destination)

    print(f"copy {source} {destination_path}")

    # copy content
    cp(source, destination_path, recursive=True)
