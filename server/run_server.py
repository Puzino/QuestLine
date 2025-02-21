import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run("run_server:app", host='0.0.0.0', port=8080, reload=True)
