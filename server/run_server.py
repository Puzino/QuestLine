from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from database.connection import Settings
from routes.auth import auth_router
from routes.game import game_router


@asynccontextmanager
async def init_database(app: FastAPI):
    await settings.initialize_database()
    yield


app = FastAPI(lifespan=init_database)
settings = Settings()
app.include_router(game_router, prefix='/game', tags=['Game'])
app.include_router(auth_router, prefix='/auth', tags=['Auth'])


@app.get("/ping")
async def ping():
    return {"message": "Pong"}


if __name__ == "__main__":
    uvicorn.run("run_server:app", host='0.0.0.0', port=8080, reload=True)
