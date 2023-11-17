import pytest

from api import depends


class TestIntegrationDynamoDB:

    @pytest.fixture
    def dynamodb(self):
        return depends.get_db()

    def test_it_should_get_a_book_from_dynamodb(self, dynamodb):
        book_id = '117a0674-0751-4f06-85df-8ede4cc99fca'
        result = dynamodb.get_book(book_id)

        assert result.id == book_id

    def test_it_should_get_all_books(self, dynamodb):
        result = dynamodb.get_books()

        assert len(result) > 0

    def test_it_should_search_a_book_by_title(self, dynamodb):
        search_term = 'Hamza'
        result = dynamodb.search_books(search_term)

        assert len(result) > 0
