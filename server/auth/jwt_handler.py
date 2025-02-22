import time
from datetime import datetime

from decouple import config
from fastapi import HTTPException, status
from jose import jwt, JWTError

SECRET_KEY = config("SECRET_KEY")
ALGORITHM = config("ALGORITHM")


def create_access_token(user: str) -> jwt:
    payload = {
        "user": user,
        "expire": time.time() + 3600
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def verify_access_token(token: str):
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        expire = data.get("expire")
        if expire is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No access token supplied"
            )
        if datetime.utcnow() > datetime.utcfromtimestamp(expire):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Token expired!"
            )
        return data
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid token."
        )
