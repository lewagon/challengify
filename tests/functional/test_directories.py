
from wagon_common.helpers.subprocess import run_command


def are_directories_identical(directory_a, directory_b):
    """
    recursively compare directory structure and file content
    """

    # compare directories
    command = [
        "diff",
        "-r",
        directory_a,
        directory_b]

    rc, output, error = run_command(command, verbose=False)

    return rc, output, error
