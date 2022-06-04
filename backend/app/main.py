import json
from loguru import logger
from fastapi import FastAPI, WebSocket, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder

from app.database.mongodb import connect_db,close_db, get_db_client
from app.matchs import routes as matchs_routes
from app.matchs import actions

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
async def websocket_endpoint(
    websocket: WebSocket, 
    match_id: str,
    player: str,
):
    db = await get_db_client()
    
    match = await db["matchs"].find_one(
        {
            "mid": match_id
        }
    )

    if not match:
        await websocket.close(
            code=status.WS_1008_POLICY_VIOLATION
        )
    
    if not player in match["players"]:
        await websocket.close(
            code=status.WS_1008_POLICY_VIOLATION
        )

    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        data = json.loads(data)
        
        if data.get("action") in actions.actions:
            await getattr(
                actions,
                data["action"]
            )(
                websocket,
                data
            )
        else:
            await websocket.send_text(
                json.dumps(
                    {
                        "mid": match["mid"],
                        "players": match["players"],
                        "moves": match["moves"],
                        "turn": match["turn"],
                        "board": match["board"],
                        "captures": match["captures"],
                        "player": match["players"].index(player)
                    }
                )
            )

            
