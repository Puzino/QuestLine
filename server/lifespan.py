from contextlib import asynccontextmanager, AsyncExitStack

from decouple import config
from fastapi import FastAPI
from redis.asyncio import Redis

from database.connection import SettingsDB

redis = None
settings = SettingsDB()


@asynccontextmanager
async def init_redis(app: FastAPI):
    global redis
    redis = Redis.from_url(config("REDIS_URL"))
    yield


@asynccontextmanager
async def init_database(app: FastAPI):
    await settings.initialize_database()
    yield


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with AsyncExitStack() as stack:
        await stack.enter_async_context(init_database(app))
        await stack.enter_async_context(init_redis(app))
        yield
