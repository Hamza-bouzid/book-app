from typing import Any

from pydantic import BaseModel


class ApiResponse(BaseModel):
    result: bool
    error_message: str = ""
    error_code: int = 0
    data: Any = {}
