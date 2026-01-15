import unittest
from contextlib import contextmanager
from unittest.mock import patch

from assertpy import assert_that
from utils import validators


class TestValidators(unittest.TestCase):
    @contextmanager
    def _silence_print(self):
        # Patch print() so validation messages don't clutter test output.
        with patch("builtins.print"):
            yield


    def test_get_int_accepts_valid_integer(self) -> None:
        # Arrange
        with patch("builtins.input", side_effect=["42"]):
            # Act
            result = validators.get_int("Enter number: ")
        # Assert
        assert_that(result).is_equal_to(42)


    def test_get_int_retries_on_invalid_input(self) -> None:
        # Arrange
        with patch("builtins.input", side_effect=["abc", "7"]), self._silence_print():
            # Act
            result = validators.get_int("Enter number: ")
        # Assert
        assert_that(result).is_equal_to(7)

    def test_get_int_in_range_accepts_valid(self) -> None:
        # Arrange
        with patch("builtins.input", side_effect=["3"]):
            # Act
            result = validators.get_int_in_range("Pick 1-5: ", 1, 5)
        # Assert
        assert_that(result).is_equal_to(3)

    def test_get_int_in_range_retries_out_of_range(self) -> None:
        # Arrange
        with patch("builtins.input", side_effect=["10", "2"]), self._silence_print():
            # Act
            result = validators.get_int_in_range("Pick 1-5: ", 1, 5)
        # Assert
        assert_that(result).is_equal_to(2)

    def test_get_non_empty_strips_and_accepts(self) -> None:
        # Arrange
        with patch("builtins.input", side_effect=["   hello  "]):
            # Act
            result = validators.get_non_empty("Enter text: ")
        # Assert
        assert_that(result).is_equal_to("hello")

    def test_get_non_empty_retries_on_blank(self) -> None:
        # Arrange
        with patch("builtins.input", side_effect=["", "   ", "ok"]), self._silence_print():
            # Act
            result = validators.get_non_empty("Enter text: ")
        # Assert
        assert_that(result).is_equal_to("ok")

    def test_get_email_accepts_basic_format(self) -> None:
        # Arrange
        with patch("builtins.input", side_effect=["user@example.com"]):
            # Act
            result = validators.get_email("Enter email: ")
        # Assert
        assert_that(result).is_equal_to("user@example.com")

    def test_get_email_retries_on_invalid(self) -> None:
        # Arrange
        with patch("builtins.input", side_effect=["invalid", "a@b", "a@b.com"]), self._silence_print():
            # Act
            result = validators.get_email("Enter email: ")
        # Assert
        assert_that(result).is_equal_to("a@b.com")

    def test_get_social_accepts_allowed_values(self) -> None:
        # Arrange
        with patch("builtins.input", side_effect=["instagram"]):
            # Act
            result = validators.get_social("Enter social: ")
        # Assert
        assert_that(result).is_equal_to("Instagram")

    def test_get_social_retries_on_invalid(self) -> None:
        # Arrange
        with patch("builtins.input", side_effect=["tiktok", "Twitter"]), self._silence_print():
            # Act
            result = validators.get_social("Enter social: ")
        # Assert
        assert_that(result).is_equal_to("Twitter")


if __name__ == "__main__":
    unittest.main()

