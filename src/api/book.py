from fastapi import APIRouter, Depends

from api import depends
from controller.BookController import BookController
from models.ApiResponse import ApiResponse
from models.BookRequest import BookRequest

router = APIRouter()


@router.get("/")
async def index() -> dict:
    return {"message": "Hello World"}


@router.post("/create")
async def create(
        book: BookRequest,
        book_controller: BookController = Depends(depends.get_book_controller),
) -> ApiResponse:
    return book_controller.create_book_from_dict(book)


@router.get("/get/{book_id}")
async def get(
        book_id: str, book_controller: BookController = Depends(depends.get_book_controller)
) -> ApiResponse:
    return book_controller.get_book_by_id(book_id)


@router.get("/get_all")
async def get_all(
        book_controller: BookController = Depends(depends.get_book_controller),
) -> ApiResponse:
    return book_controller.get_all_books()


@router.delete("/delete/{book_id}")
async def delete(
        book_id: str, book_controller: BookController = Depends(depends.get_book_controller)
) -> ApiResponse:
    return book_controller.delete_book_by_id(book_id)


@router.patch("/update/{book_id}")
async def update(
        book_id: str,
        book: dict,
        book_controller: BookController = Depends(depends.get_book_controller),
) -> ApiResponse:
    return book_controller.update_book_by_id(book_id, book)
