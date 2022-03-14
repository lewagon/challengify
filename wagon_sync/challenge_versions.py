
from wagon_sync.challenge_version import ChallengeVersion


class ChallengeVersions:
    """
    stores all existing challenge versions
    stores range of versions on which to run the script
    allows to iterate on challenge versions
    allows to iterate on delimiter versions
    """

    def __init__(self, challenge_versions):

        self.versions = [ChallengeVersion(v) for v in challenge_versions]
        self.min_version = 0
        self.max_version = len(self.versions)

    def __find_version_index(self, version, min=False):
        """
        allows to access version from name or index
        """

        if version is None:
            if min:
                return 0
            else:
                return len(self.versions)

        if type(version) is int:
            return version

        if type(version) is str:
            return self.version.index(version)

        raise TypeError(f"Unsupported version type {type(version)}")

    def filter(self, min_version, max_version):
        """
        filters versions on which to run the script
        """

        self.min_version = self.__find_version_index(min_version, min=True)
        self.max_version = self.__find_version_index(max_version)

        return self

    def __iter__(self):
        """
        iterator initializer
        """

        self.n = self.min_version
        return self

    def __next__(self):
        """
        iterator increment
        """

        if self.n < self.max_version:
            result = self.versions[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration

    def __getitem__(self, key):
        """
        element access by slice or index
        """

        if isinstance(key, slice):
            print(key)
            return self.versions[key]

        if isinstance(key, int):
            print(f"kkk{key}")
            return self.versions[key]

        raise TypeError("Invalid argument type.")
