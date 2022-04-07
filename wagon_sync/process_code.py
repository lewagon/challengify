
from wagon_sync.challengify import Challengify
from wagon_sync.file import File

from wagon_common.helpers.file import ensure_path_directory_exists


def process_code(
        challengify: Challengify,
        source, destination, file_extension, version_iterator=None):

    # create destination directory
    ensure_path_directory_exists(destination)

    # create file scope
    file_scope = [File(source, destination, file_extension)]

    # run challengify
    if version_iterator is None:

        # process file scope
        challengify.process(file_scope)

    # run challengify iterate
    else:

        # iterate through scope
        for file in file_scope:
            file.challengify_iterate(version_iterator)
