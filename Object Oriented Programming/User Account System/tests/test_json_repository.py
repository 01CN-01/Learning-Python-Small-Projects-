import json
import tempfile
import unittest
from assertpy import assert_that
from models.user import User
from storage.json_repository import JsonUserRepository


class TestJsonUserRepository(unittest.TestCase):
    def _make_repo(self, initial_payload: dict | None = None) -> JsonUserRepository:
        # Create a temp file and optionally seed it with JSON data.
        temp_file = tempfile.NamedTemporaryFile(delete=True)
        if initial_payload is not None:
            with open(temp_file.name, "w") as file_handle:
                json.dump(initial_payload, file_handle)
        return JsonUserRepository(temp_file.name)

    def test_save_and_load_round_trip(self) -> None:
        # Arrange
        repo = self._make_repo()
        users = [
            User("Instagram", "Jane", "Doe", "jane@example.com", "pw"),
            User("Facebook", "John", "Doe", "john@example.com", "pw"),
        ]

        # Act
        repo.save_all(users)
        loaded = repo.load_all()

        # Assert
        assert_that(loaded).is_length(2)
        assert_that(loaded[0].email).is_equal_to("jane@example.com")
        assert_that(loaded[1].email).is_equal_to("john@example.com")

    def test_load_all_handles_missing_file(self) -> None:
        # Arrange
        temp_file = tempfile.NamedTemporaryFile(delete=True)
        repo = JsonUserRepository(temp_file.name)

        # Act
        loaded = repo.load_all()

        # Assert
        assert_that(loaded).is_empty()

    def test_load_all_supports_legacy_keys(self) -> None:
        # Arrange
        legacy_payload = {
            "user_account": [
                {
                    "social": "Instagram",
                    "firstname": "Legacy",
                    "lastname": "User",
                    "email": "legacy@example.com",
                    "password": "pw",
                }
            ]
        }
        repo = self._make_repo(initial_payload=legacy_payload)

        # Act
        loaded = repo.load_all()

        # Assert
        assert_that(loaded).is_length(1)
        assert_that(loaded[0].first_name).is_equal_to("Legacy")
        assert_that(loaded[0].last_name).is_equal_to("User")

