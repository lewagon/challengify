
from wagon_sync.challenge_versions import ChallengeVersions

import pytest


class TestChallengeVersions:
    """
    test challenge versions
    """

    @pytest.fixture
    def challenge_versions(self):

        # Arrange
        # TODO: replace with loader object
        loaded_priorities = dict(
            base="07-ML-Ops/01-Train-at-scale/04-Investigating-bottlenecks",
            api="07-ML-Ops/04-Predict-in-production/01-Build-your-API",
            docker_image="07-ML-Ops/04-Predict-in-production/02-Docker-image",
            docker_prod="07-ML-Ops/04-Predict-in-production/03-Deploy-to-Cloud-Run",
            api_advanced="07-ML-Ops/04-Predict-in-production/04-API-advanced")

        challenge_versions = ChallengeVersions(list(loaded_priorities))

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

    def test_filter(self, challenge_versions):

        # Act
        challenge_versions.filter(1, 3)

        # Assert
        stored_versions = [c.version for c in challenge_versions.versions]
        iterable_versions = [c.version for c in challenge_versions]

        assert stored_versions == self.loaded_versions
        assert iterable_versions == self.loaded_versions[1:3]

    def test_slices(self, challenge_versions):

        # Act
        # none

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
