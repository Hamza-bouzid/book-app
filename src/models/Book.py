import datetime
import uuid

from pydantic import BaseModel


class Book(BaseModel):
    id: str
    title: str
    author: str
    is_read: bool
    created_at: datetime.datetime

    def to_dynamodb_dict(self):
        return {
            "id": {"S": self.id},
            "title": {"S": self.title},
            "author": {"S": self.author},
            "is_read": {"BOOL": self.is_read},
            "created_at": {"N": str(int(self.created_at.timestamp()))},
        }

    @staticmethod
    def from_book_request(book_request):
        return Book(
            id=str(uuid.uuid4()),
            title=book_request.title,
            author=book_request.author,
            is_read=False,
            created_at=datetime.datetime.now(),
        )

    @staticmethod
    def from_dynamodb_item(item):
        return Book(
            id=item["id"]["S"],
            title=item["title"]["S"],
            author=item["author"]["S"],
            is_read=item["is_read"]["BOOL"],
            created_at=datetime.datetime.fromtimestamp(int(item["created_at"]["N"])),
        )
