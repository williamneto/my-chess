from loguru import logger
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware

from app.database.mongodb import connect_db,close_db
from app.matchs import routes as matchs_routes

origins = ["*"]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.add_event_handler("startup", connect_db)
app.add_event_handler("shutdown", close_db)

app.include_router(matchs_routes.router)

@app.websocket("/match")
async def websocket_endpoint(websocket: WebSocket, match_id: str):
    logger.info(match_id)
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
