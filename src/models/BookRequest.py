from pydantic import BaseModel


class BookRequest(BaseModel):
    title: str
    author: str
    # to_finish_date: str
    # genre: str
