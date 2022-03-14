
from wagon_sync.challenge_version import ChallengeVersion

from colorama import Fore, Style


class ChallengeVersionIterator:
    """
    stores all existing challenge versions
    stores range of versions on which to run the script
    allows to iterate on challenge versions
    allows to iterate on delimiter versions
    """

    def __init__(self, destinations):

        self.versions = [ChallengeVersion(v, i, d) for i, (v, d) in enumerate(destinations.items())]
        self.positions = {c.version:c.position for c in self.versions}
        self.min_position = 0
        self.max_position = len(self.versions)

    def filter(self, min_position, max_position):
        """
        filters versions on which to run the script
        """

        self.min_position = self.__find_version_index(min_position, min=True)
        self.max_position = self.__find_version_index(max_position) + 1  # excluded

        return self

    def position(self, version):

        if version not in self.positions:

            print(Fore.RED
                  + "\nVersion does not exist 🤕"
                  + Style.RESET_ALL
                  + f"\nPlease verify that the version {version} is declared in the `destination` section of the conf file.")

        return self.positions[version]

    def __find_version_index(self, version, min=False):
        """
        allows to access version from name or index
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
