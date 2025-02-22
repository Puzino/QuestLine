from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from auth.hash_password import HashPassword
from auth.jwt_handler import create_access_token
from database.connection import write_to_database, read_database
from models.auth import TokenResponse, User

auth_router = APIRouter()
hash_password = HashPassword()

users = read_database()


@auth_router.post('/register')
async def sing_new_user(user: User) -> dict:
    user_exist = users.get(user.username)
    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with suplied login already exists"
        )
    hashed_password = hash_password.create_hash(user.password)
    user.password = hashed_password
    write_to_database(user)
    return {"message": "User created successfully."}


@auth_router.post('/login', response_model=TokenResponse)
async def login(user: OAuth2PasswordRequestForm = Depends()) -> dict:
    user_exist = User(**users)
    if not user_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with email does not exist."
        )
    if hash_password.verify_hash(user.password, user_exist.password):
        access_token = create_access_token(user_exist.username)
        return {"access_token": access_token, "token_type": "Bearer"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid details passed."
    )
