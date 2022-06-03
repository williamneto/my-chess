import json
from loguru import logger

from app.database.mongodb import get_db_client
actions = [
    "player_move"
]

async def player_move(websocket, payload):
    db = await get_db_client()

    match = await db["matchs"].find_one(
        {
            "mid": payload["mid"]
        }
    )

    nextTurn = None
    if payload["player"] == match["turn"]:
        if match["turn"] == 0:
            nextTurn = 1
        else:
            nextTurn = 0

        match["moves"].append(
            payload["move"]
        )
        match["turn"] = nextTurn

        await db["matchs"].update_one(
            {
                "mid": match["mid"]
            }, {
                "$set": {
                    "moves": match["moves"],
                    "turn": nextTurn
                }
            }
        )

        await websocket.send_text(
            json.dumps(
                {
                    "mid": match["mid"],
                    "players": match["players"],
                    "moves": match["moves"],
                    "turn": match["turn"],
                    "player": match["players"].index(match["players"][payload["player"]])
                }
            )
        )