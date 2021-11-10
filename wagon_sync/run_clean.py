
import os
import glob

from colorama import Fore, Style

from wagon_sync.params.delimiters import TEST_CHALLENGIFICATION_PATTERNS


def clean_test_challengifications():
    """
    remove test challengifications in the current directory
    """

    # match pattern
    all_matches = []

    for test_challengification_pattern in TEST_CHALLENGIFICATION_PATTERNS:

        # retrieve files matching pattern
        matches = glob.glob(test_challengification_pattern, recursive=True)

        all_matches += matches

    if len(all_matches) == 0:

        print(Fore.GREEN
              + "\nNo matches found 🎉"
              + Style.RESET_ALL)

        return

    print(Fore.BLUE
          + "\nMatches deleted:"
          + Style.RESET_ALL)

    # iterate through results
    for file_path in all_matches:

        print(f"- {file_path}")

        # remove file
        os.remove(file_path)
