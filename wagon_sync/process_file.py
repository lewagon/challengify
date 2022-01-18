
from wagon_common.helpers.file import cp


def process_file(source, destination, file_extension, ignore_run_delimiters, version_pre_clean=None):

    # copy file
    cp(source, destination)
