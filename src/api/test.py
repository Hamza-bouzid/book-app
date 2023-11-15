from fastapi import APIRouter

router = APIRouter()


@router.get("/test", tags=["test"])
async def root():
    return {"message": "Hello World"}
