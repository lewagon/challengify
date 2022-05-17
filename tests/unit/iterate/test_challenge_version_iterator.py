
from wagon_sync.challenge_version_iterator import ChallengeVersionIterator

import pytest


class TestChallengeVersions:
    """
    test challenge versions
    """

    @pytest.fixture
    def challenge_versions(self):

        # Arrange
        # TODO: replace with loader object
        destinations = dict(
            base="07-ML-Ops/01-Train-at-scale/04-Investigating-bottlenecks",
            api="07-ML-Ops/04-Predict-in-production/01-Build-your-API",
            docker_image="07-ML-Ops/04-Predict-in-production/02-Docker-image",
            docker_prod="07-ML-Ops/04-Predict-in-production/03-Deploy-to-Cloud-Run",
            api_advanced="07-ML-Ops/04-Predict-in-production/04-API-advanced")

        challenge_versions = ChallengeVersionIterator(destinations)

        self.loaded_versions = ["base", "api", "docker_image", "docker_prod", "api_advanced"]

        # Act & Assert
        yield challenge_versions

        # Cleanup
        # none

    def test_load(self, challenge_versions):

        # Act
        # none

        # Assert
        stored_versions = [c.version for c in challenge_versions.versions]
        iterable_versions = [c.version for c in challenge_versions]

        assert stored_versions == self.loaded_versions
        assert iterable_versions == self.loaded_versions

    def test_multiple_iterations(self, challenge_versions):
        """
        ensure multiple iterations run correctly
        """

        # Act
        # none

        # Assert
        stored_versions = [c.version for c in challenge_versions.versions]
        stored_versions_2 = [c.version for c in challenge_versions.versions]
        iterable_versions = [c.version for c in challenge_versions]
        iterable_versions_2 = [c.version for c in challenge_versions]

        assert stored_versions == self.loaded_versions
        assert stored_versions_2 == self.loaded_versions
        assert iterable_versions == self.loaded_versions
        assert iterable_versions_2 == self.loaded_versions

    def test_filter(self, challenge_versions):

        # Act
        challenge_versions.filter(1, 3)

        # Assert
        stored_versions = [c.version for c in challenge_versions.versions]
        iterable_versions = [c.version for c in challenge_versions]

        assert stored_versions == self.loaded_versions
        assert iterable_versions == self.loaded_versions[1:4]

    def test_filter_str(self, challenge_versions):

        # Act
        challenge_versions.filter("api", "api_advanced")

        # Assert
        stored_versions = [c.version for c in challenge_versions.versions]
        iterable_versions = [c.version for c in challenge_versions]

        assert stored_versions == self.loaded_versions
        assert iterable_versions == self.loaded_versions[1:5]

    def test_slices(self, challenge_versions):

        # Act
        # none

        # Assert
        stored_versions = [c.version for c in challenge_versions.versions]
        slice_versions = [c.version for c in challenge_versions[0:4]]

        assert stored_versions == self.loaded_versions
        assert slice_versions == self.loaded_versions[0:4]

    def test_filter_and_slices(self, challenge_versions):

        # Act
        challenge_versions.filter(1, 3)

        # Assert
        stored_versions = [c.version for c in challenge_versions.versions]
        slice_versions = [c.version for c in challenge_versions[0:4]]

        assert stored_versions == self.loaded_versions
        assert slice_versions == self.loaded_versions[0:4]

    def test_get(self, challenge_versions):

        # Act
        # none

        # Assert
        stored_versions = [c.version for c in challenge_versions.versions]
        slice_versions = challenge_versions[-1].version

        assert stored_versions == self.loaded_versions
        assert slice_versions == self.loaded_versions[-1]

    def test_versions_1_iteration(self, challenge_versions):

        # Act
        iterator = iter(challenge_versions)
        first = next(iterator)

        # Assert
        assert first.version == self.loaded_versions[0]

        versions_before = []
        version_current = "base"
        versions_after = ["api", "docker_image", "docker_prod", "api_advanced"]

        assert challenge_versions.get_versions_before() == versions_before
        assert challenge_versions.get_version_current() == version_current
        assert challenge_versions.get_versions_after() == versions_after

    def test_versions_4_iterations(self, challenge_versions):

        # Act
        iterator = iter(challenge_versions)
        first = next(iterator)
        second = next(iterator)
        third = next(iterator)
        fourth = next(iterator)

        # Assert
        assert first.version == self.loaded_versions[0]
        assert second.version == self.loaded_versions[1]
        assert third.version == self.loaded_versions[2]
        assert fourth.version == self.loaded_versions[3]

        versions_before = ["base", "api", "docker_image"]
        version_current = "docker_prod"
        versions_after = ["api_advanced"]

        assert challenge_versions.get_versions_before() == versions_before
        assert challenge_versions.get_version_current() == version_current
        assert challenge_versions.get_versions_after() == versions_after
