import os
import secrets
from typing import Optional

from dotenv import load_dotenv
from fastapi import Header, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette import status

load_dotenv()

http_basic = HTTPBasic()


def basic_auth(credentials: HTTPBasicCredentials = Depends(http_basic), authorization: Optional[str] = Header(None)):
    if not authorization:
        raise_unauthorized()
    correct_username = secrets.compare_digest(credentials.username, os.getenv('BASIC_AUTH_USERNAME'))
    correct_password = secrets.compare_digest(credentials.password, os.getenv('BASIC_AUTH_PASSWORD'))
    if not (correct_username and correct_password):
        raise_unauthorized()
    return True


def raise_unauthorized(detail: str = "Not authorized", headers: dict = None) -> HTTPException:
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=detail,
        headers=headers
    )
