import uvicorn
from fastapi import FastAPI

from routes.auth import auth_router
from routes.game import game_router

app = FastAPI()
app.include_router(game_router, prefix='/game', tags=['Game'])
app.include_router(auth_router, prefix='/auth', tags=['Auth'])


@app.get("/")
async def root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run("run_server:app", host='0.0.0.0', port=8080, reload=True)
