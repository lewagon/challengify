
from wagon_sync.challenge_version import ChallengeVersion

from colorama import Fore, Style


class ChallengeVersionIterator:
    """
    stores all existing challenge versions
    stores filtered range of versions on which to run the script
    allows to iterate on filtered challenge versions (default)
    allows to iterate on all challenge versions (used for delimiters)
    """

    def __init__(self, destinations):

        self.versions = [ChallengeVersion(v, i, d) for i, (v, d) in enumerate(destinations.items())]
        self.positions = {c.version:c.position for c in self.versions}
        self.min_position = 0
        self.max_position = len(self.versions)

    def filter(self, min_position, max_position):
        """
        filters versions on which to run the script by name or sequence position
        """

        self.min_position = self.__find_version_index(min_position, min=True)
        self.max_position = self.__find_version_index(max_position) + 1  # excluded

        return self

    def position(self, version):
        """
        returns version sequence position from name or sequence position
        """

        # check if param is a number
        if version.isdigit():

            version = int(version)

            if version < 0 or version >= len(self.versions):

                print(Fore.RED
                      + "\nInvalid version 🤕"
                      + Style.RESET_ALL
                      + f"\nPlease verify that the version {version} corresponds to a valid sequence in the `destination` section of the conf file.")

                raise ValueError("Invalid version")

            return version

        # verify if version exists
        if version not in self.positions:

            print(Fore.RED
                  + "\nVersion does not exist 🤕"
                  + Style.RESET_ALL
                  + f"\nPlease verify that the version {version} is declared in the `destination` section of the conf file.")

        return self.positions[version]

    def __find_version_index(self, version, min=False):
        """
        allows to access version by name or sequence position
        """

        if version is None:
            if min:
                return 0
            else:
                return len(self.versions) - 1  # included

        if type(version) is int:
            return version

        if type(version) is str:
            return self.position(version)

        raise TypeError(f"Unsupported version type {type(version)}")

    def __iter__(self):
        """
        iterator initializer
        """

        self.iterated_position = self.min_position
        return self

    def __next__(self):
        """
        iterator increment
        """

        if self.iterated_position < self.max_position:
            result = self.versions[self.iterated_position]
            self.iterated_position += 1
            return result
        else:
            raise StopIteration

    def __getitem__(self, key):
        """
        element access by slice or index
        """

        if isinstance(key, slice):
            return self.versions[key]

        if isinstance(key, int):
            return self.versions[key]

        raise TypeError("Invalid argument type.")
