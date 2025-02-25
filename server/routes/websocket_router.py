import json
from json import JSONDecodeError

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from database.connection import Database
from models.chat import Message
from ws_manager.manager import ConnectionManager

ws_router = APIRouter()

manager = ConnectionManager()
chat_database = Database(Message)


@ws_router.websocket("/chat/{chat_id}")
async def websocket_chat(websocket: WebSocket, chat_id: int):
    from lifespan import redis
    await manager.connect(chat_id, websocket)
    try:
        while True:
            try:
                data = await websocket.receive_json()
            except JSONDecodeError:
                continue
            message_object = Message(chat_id=chat_id, user=data.get("user"), content=data.get("message"))
            await redis.lpush(f"chat:{chat_id}:messages",
                              json.dumps(message_object.model_dump(), ensure_ascii=False, default=str))
            await chat_database.save(message_object)
            await manager.broadcast(chat_id, f"Client #{message_object.user} says: {message_object.content}")
    except WebSocketDisconnect:
        await manager.disconnect(chat_id, websocket)
        await manager.broadcast(chat_id, f"Client #{message_object.user} left the chat")
