"""
runs sync on a specified file
"""

from wagon_sync.process_notebook import process_notebook
from wagon_sync.process_code import process_code
from wagon_sync.process_file import process_file

from wagon_sync.params.delimiters import TEST_CHALLENGIFICATION_SUFFIX

import os


def process(
        file_path, destination,
        ignore_run_delimiters,
        ignore_tld, iterate_yaml_path,
        test, version_pre_clean=None):
    """
    process file extension and process it accordingly
    """

    # buid destination file path
    if test:

        # ignore destination and relocate all test challengifications
        # next to the source file
        destination = "."

        # retrieve file root and extension
        file_path_root, file_path_extension = os.path.splitext(file_path)

        # build test challengification filename
        destination_file_path = (
            file_path_root + TEST_CHALLENGIFICATION_SUFFIX + file_path_extension)

    else:

        destination_file_path = file_path

    # correct destination path
    if ignore_tld:

        # correct destination path relative to iterate yaml path
        destination_file_path = os.path.relpath(destination_file_path, iterate_yaml_path)

    # build destination path
    destination_path = os.path.join(
        destination,
        destination_file_path)

    print(f"{file_path} {os.path.relpath(destination_path)}")

    # get file extension
    _, ext = os.path.splitext(file_path)

    # checking filenames without an extension
    if ext == "":

        # default profile for extensionless or dot files is shell
        ext = ".sh"

    # extension handlers
    handlers = dict(
        ipynb=process_notebook,
        py=process_code,
        rb=process_code,
        sh=process_code,
        txt=process_code,
        )

    # retrieve handler function
    file_extension = ext[1:]
    handler_function = handlers.get(file_extension, process_file)  # default handler

    # call handler
    handler_function(
        file_path,
        destination_path,
        file_extension,
        ignore_run_delimiters,
        version_pre_clean=version_pre_clean)

    return destination_path
