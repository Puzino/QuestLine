from datetime import datetime

from beanie import Document


class Message(Document):
    chat_id: int
    user: str
    content: str
    timestamp: datetime = datetime.now()

    class Settings:
        name = "messages"
