import uvicorn
from fastapi import FastAPI
from database.connection import SettingsDB
from lifespan import lifespan
from routes.auth import auth_router
from routes.game import game_router
from routes.websocket_router import ws_router

app = FastAPI(lifespan=lifespan)

settings = SettingsDB()

app.include_router(game_router, prefix='/game', tags=['Game'])
app.include_router(auth_router, prefix='/auth', tags=['Auth'])
app.include_router(ws_router, prefix='/ws', tags=['Chat'])


@app.get("/ping")
async def ping():
    return {"message": "Pong"}


if __name__ == "__main__":
    uvicorn.run("run_server:app", host='0.0.0.0', port=8080, reload=True)
