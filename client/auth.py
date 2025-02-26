import requests
from decouple import config
from requests import RequestException

SERVER_URL = config("SERVER_URL")
WEBSOCKET_URL = config("WEBSOCKET_URL")


def save_auth():
    # if not os.path.exists(os.path.join(Path(__file__), AUTH_CONFIG_NAME)):
    #     pass
    pass


def register(username: str, password: str) -> str:
    data = {"username": username, "password": password}
    try:
        response = requests.post(f"{SERVER_URL}/auth/register", json=data)
        response_data = response.json()
        if response.status_code in (409, 422):
            raise ValueError(response_data.get("detail"), "Unknown error")
        response.raise_for_status()
        return response_data.get("message")
    except RequestException as ex:
        raise Exception(f"Failed: {ex}")


def login(username: str, password: str) -> str | None:
    data = {"username": username, "password": password}
    response = requests.post(f"{SERVER_URL}/auth/login", data=data)
    if response.status_code == 200:
        token = response.json().get("access_token")
        return f"Bearer {token}"
    return None
