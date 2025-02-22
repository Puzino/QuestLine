import json

import requests
from decouple import config

SERVER_URL = config("SERVER_URL")
WEBSOCKET_URL = config("WEBSOCKET_URL")


def register(username: str, password: str) -> json:
    data = {"username": username, "password": password}
    response = requests.post(f"{SERVER_URL}/auth/register", json=data)
    return response.json()


def login(username: str, password: str) -> str | None:
    data = {"username": username, "password": password}
    response = requests.post(f"{SERVER_URL}/auth/login", data=data)
    if response.status_code == 200:
        return f"Bearer {response.json()["access_token"]}"
    return None
