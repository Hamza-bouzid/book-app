from fastapi import APIRouter, Depends

from src.api import book, test
from src.api.auth import basic_auth

router = APIRouter()
router.include_router(test.router, prefix="/test", tags=["test"])
router.include_router(
    book.router, prefix="/book", tags=["book"], dependencies=[Depends(basic_auth)]
)
