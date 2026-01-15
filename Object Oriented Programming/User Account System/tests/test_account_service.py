import tempfile
import unittest
from assertpy import assert_that
from models.user import User
from services.account_service import AccountService
from storage.json_repository import JsonUserRepository


class TestAccountService(unittest.TestCase):
    def _make_service(self) -> AccountService:
        # Create a temporary file for each test to avoid sharing data.
        temp_file = tempfile.NamedTemporaryFile(delete=True)
        repository = JsonUserRepository(temp_file.name)
        return AccountService(repository)

    def test_add_user_persists_in_list(self) -> None:
        # Arrange
        service = self._make_service()
        user = User("Instagram", "Jane", "Doe", "jane@example.com", "pw")

        # Act
        service.add_user(user)

        # Assert
        users = service.list_users()
        assert_that(users).is_length(1)
        assert_that(users[0].email).is_equal_to("jane@example.com")

    def test_remove_user_by_index(self) -> None:
        # Arrange
        service = self._make_service()
        service.add_user(User("Facebook", "Ava", "Smith", "a@b.com", "pw"))
        service.add_user(User("Twitter", "Noah", "Lee", "n@b.com", "pw"))

        # Act
        result = service.remove_user_by_index(0)

        # Assert
        assert_that(result).is_true()
        assert_that(service.list_users()).is_length(1)
        assert_that(service.list_users()[0].social).is_equal_to("Twitter")

    def test_remove_user_by_index_out_of_range(self) -> None:
        # Arrange
        service = self._make_service()
        service.add_user(User("Snapchat", "Kai", "Rae", "k@b.com", "pw"))

        # Act
        result = service.remove_user_by_index(5)

        # Assert
        assert_that(result).is_false()
        assert_that(service.list_users()).is_length(1)

    def test_search_by_social_is_case_insensitive(self) -> None:
        # Arrange
        service = self._make_service()
        service.add_user(User("Instagram", "Eva", "Stone", "e@b.com", "pw"))
        service.add_user(User("Facebook", "Leo", "Park", "l@b.com", "pw"))

        # Act
        results = service.search_by_social("instagram")

        # Assert
        assert_that(results).is_length(1)
        assert_that(results[0].first_name).is_equal_to("Eva")

    def test_search_by_name_matches_first_or_last(self) -> None:
        # Arrange
        service = self._make_service()
        service.add_user(User("Discord", "Mia", "Lopez", "m@b.com", "pw"))
        service.add_user(User("Discord", "Sam", "Mia", "s@b.com", "pw"))

        # Act
        results = service.search_by_name("mia")

        # Assert
        assert_that(results).is_length(2)

