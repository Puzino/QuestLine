from beanie import Document
from pydantic import BaseModel


class User(Document):
    player_id: str = None
    username: str
    password: str

    class Settings:
        name = "users"


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
