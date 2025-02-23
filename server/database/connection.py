from beanie import init_beanie
from decouple import config
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel

from models.auth import User


class Settings:
    DATABASE_URL: str = config("DATABASE_URL")

    async def initialize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(database=client.get_default_database(), document_models=[User])


class Database:
    def __init__(self, model):
        self.model = model

    async def save(self, document):
        await document.create()
        return

    async def get(self, _id: str):
        doc = await self.model.get(_id)
        if doc:
            return doc
        return False

    async def get_all(self):
        docs = await self.model.find_all().to_list()
        return docs

    async def update(self, _id: str, body: BaseModel):
        doc_id = _id
        des_body = body.model_dump()

        des_body = {k: v for k, v in des_body.items() if v is not None}
        update_query = {"$set": {field: value for field, value in des_body.items()}}
        doc = await self.get(doc_id)
        if not doc:
            return False
        await doc.update(update_query)
        return doc

    async def delete(self, _id: str):
        doc = await self.get(_id)
        if not doc:
            return False
        await doc.delete()
        return True
