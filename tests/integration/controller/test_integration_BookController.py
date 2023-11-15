import pytest

from src.api import depends
from src.models.BookRequest import BookRequest


class TestIntegrationBookController:

    @pytest.fixture
    def book_controller(self):
        return depends.get_book_controller()

    def test_it_should_create_a_book_in_dynamodb(self, book_controller):
        book_request = BookRequest(
            title="test_integration",
            author="test",

        )

        result = book_controller.create_book_from_dict(book_request)

        assert result.result is True
