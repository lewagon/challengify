"""
runs sync on a specified file
"""

from wagon_sync.challengify import Challengify

from wagon_sync.process_notebook import process_notebook
from wagon_sync.process_code import process_code
from wagon_sync.process_file import process_file

from wagon_sync.params.delimiters import TEST_CHALLENGIFICATION_SUFFIX

import os


def get_file_extension(file_path):

    # get file extension
    file_root, ext = os.path.splitext(file_path)

    # checking filenames without an extension
    if ext == "":

        # default profile for extensionless or dot files is shell
        ext = ".sh"

    # checking erb extensions
    if ext == ".erb":

        # get sub extension
        _, subext = os.path.splitext(file_root)

        ext = f"{subext}{ext.replace('.', '_')}"

    return ext[1:]


def process(
        challengify: Challengify,
        file_path, destination, target_file_path, dry_run,
        ignore_tld, iterate_yaml_path,
        test, version_iterator=None):
    """
    process file extension and process it accordingly
    """

    # buid destination file path
    if test:

        # ignore destination and relocate all test challengifications
        # next to the source file
        destination = "."

        # retrieve file root and extension
        file_path_root, file_path_extension = os.path.splitext(target_file_path)

        # build test challengification filename
        destination_file_path = (
            file_path_root + TEST_CHALLENGIFICATION_SUFFIX + file_path_extension)

    else:

        destination_file_path = target_file_path

    # correct destination path
    if ignore_tld:

        # correct destination path relative to iterate yaml path
        destination_file_path = os.path.relpath(destination_file_path, iterate_yaml_path)

    # build destination path
    destination_path = os.path.join(
        destination,
        destination_file_path)

    print(f"{file_path} {os.path.relpath(destination_path)}")

    # extension handlers
    handlers = {
        process_notebook: ["ipynb"],
        process_code: [
            "",  # extensionless files
            "py", "rb", "sh", "txt", "md", "sample",
            "yml", "yaml", "toml",
            "html", "css", "js", "html_erb", "js_erb"]}

    # retrieve handler function
    file_extension = get_file_extension(file_path)
    possible_handlers = [function for function, extensions in handlers.items() if file_extension in extensions]
    handler_function = possible_handlers[0] if len(possible_handlers) > 0 else process_file  # default handler
    # handler_function = handlers.get(file_extension, process_file)  # default handler

    # call handler
    if not dry_run:

        handler_function(
            challengify,
            file_path,
            destination_path,
            file_extension,
            version_iterator=version_iterator)

    return destination_file_path, destination_path
