
from wagon_sync.challengify import Challengify

from wagon_common.helpers.file import cp


def process_file(
        challengify: Challengify,
        source, destination, file_extension, version_iterator=None):

    # copy file
    cp(source, destination)
