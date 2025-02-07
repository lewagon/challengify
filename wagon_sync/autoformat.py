
from wagon_common.helpers.subprocess import run_command

from colorama import Fore, Style


def format_python_code_files(files):
    """
    use python autoformatter on files
    """

    # format python code
    command = [
        "black",
        "-q",       # quiet mode
        ] + files

    rc, output, error = run_command(command, verbose=True)

    return rc == 0, rc, output, error


def autoformat_code(files):
    """
    run code autoformatter on files
    """

    # python formatter
    target_files = [file for file in files if file[-3:] == ".py"]

    formatted, rc, output, error = format_python_code_files(target_files)

    if not formatted:

        print(Fore.RED
              + f"\nError autoformatting python code ❌"
              + Style.RESET_ALL
              + f"\n- rc: {rc}"
              + f"\n- output: {output}"
              + f"\n- error: {error}")

    # ruby formatter
    # TODO
