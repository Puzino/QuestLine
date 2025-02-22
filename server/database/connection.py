# TODO: Make a MongoDB|PostgreSQL database
import json
import os
from pathlib import Path

from models.auth import User

DATABASE_NAME = "database.json"
DATABASE_PATH = os.path.join(Path(__file__).parent.parent, DATABASE_NAME)


def write_to_database(user: User) -> None:
    with open(os.path.join(DATABASE_PATH), 'w', encoding='utf-8') as file:
        json.dump(dict(user), file, ensure_ascii=False, indent=4)


def read_database() -> dict:
    with open(os.path.join(DATABASE_PATH), 'r', encoding='utf-8') as file:
        return json.load(file)
