import json
from loguru import logger

from app.database.mongodb import get_db_client
actions = [
    "player_move"
]

async def player_move(websocket, payload):
    def validate_move(match, move):
        move = move.split("|")
        valid = True

        # Verificar se a peça movimenta está na casa referida
        if match["board"][move[0]] != move[1]:
            valid = False

        # Verificar se a peça movimentada pode se mover a casa de destino
        
        return valid

    def update_board(match, move):
        # Verificar se o movimento é de captura
        # Se for, salva a captura, posiciona a peça no destino e
        # remove da casa de partida
        # Se não for, posiciona a peça no destino e 
        # remove da casa de partida

        move = move.split("|")
        if match["board"][move[2]]:
            match["captures"][str(payload["player"])].append(
                match["board"][move[2]]
            )
        
        match["board"][move[2]] = move[1]
        match["board"][move[0]] = ""

        return match
        
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

        if validate_move(match, payload["move"]):
            match = update_board(
                match,
                payload["move"]
            )
            match["moves"].append(
                payload["move"]
            )
            match["turn"] = nextTurn

            await db["matchs"].update_one(
                {
                    "mid": match["mid"]
                }, {
                    "$set": {
                        "board": match["board"],
                        "captures": match["captures"],
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
                        "board": match["board"],
                        "captures": match["captures"],
                        "player": match["players"].index(match["players"][payload["player"]])
                    }
                )
            )
        else:
            await websocket.send_text(
                json.dumps(
                    {
                        "error": "invalid-move"
                    }
                )
            )
    else:
        await websocket.send_text(
            json.dumps(
                {
                    "error": "invalid-turn"
                }
            )
        )