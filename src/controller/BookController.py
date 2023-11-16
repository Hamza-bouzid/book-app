from controller import DownloadController
from controller.UploadImageController import UploadImageController
from models.ApiResponse import ApiResponse
from models.Book import Book
from models.BookRequest import BookRequest
from repositories import DynamoDB


class BookController:
    def __init__(
        self,
        upload_image_controller: UploadImageController,
        download_controller: DownloadController,
        db: DynamoDB,
    ):
        self.upload_image_controller = upload_image_controller
        self.download_controller = download_controller
        self.db = db

    def create_book_from_dict(self, book_request: BookRequest) -> ApiResponse:
        book = Book.from_book_request(book_request)
        book_dict = book.to_dynamodb_dict()
        self.db.create_book(book_dict)
        return ApiResponse(result=True, data=book_dict)

    def get_book_by_id(self, book_id: str) -> ApiResponse:
        book = self.db.get_book(book_id)
        if not book:
            return ApiResponse(result=False, data={"message": "Book not found"})
        return ApiResponse(result=True, data=book)

    def get_all_books(self) -> ApiResponse:
        books = self.db.get_books()
        return ApiResponse(result=True, data=books)

    def delete_book_by_id(self, book_id: str) -> ApiResponse:
        book = self.db.delete_book(book_id)
        return ApiResponse(result=True, data=book)

    def update_book_by_id(self, book_id: str, book_dict: dict) -> ApiResponse:
        book = self.db.update_book(book_id, book_dict)
        return ApiResponse(result=True, data=book)
