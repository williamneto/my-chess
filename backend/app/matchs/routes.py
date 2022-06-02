import uuid, re
from loguru import logger
from fastapi import APIRouter, status, Request, HTTPException
from fastapi.encoders import jsonable_encoder

from app.database.mongodb import get_db_client
from app.core.config import settings

router = APIRouter(
    prefix="/matchs"
)

@router.get("/new")
async def new_match():
    db = await get_db_client()

    match_id = str(uuid.uuid4())
    match_url = "%s/matchs/%s" % (
        settings.PUBLIC_URL,
        match_id
    )

    match = {
        "mid": match_id,
        "url": match_url,
        "players": []
    }

    await db["matchs"].insert_one(
        jsonable_encoder(match)
    )

    return match

@router.get("/{match_id}")
async def enter_match(match_id: str, req: Request):
    db = await get_db_client()
    client_ip = req.client.host

    match = await db["matchs"].find_one(
        {
            "mid": match_id
        }, {'_id': 0}
    )
    if not match:
        raise HTTPException(
            status_code=404
        )

    if len(match["players"]) == 2 and not client_ip in match["players"]:
        raise HTTPException(
            status_code=404
        )
    elif len(match["players"]) < 2 and not client_ip in match["players"]:
        match["players"].append(client_ip)
        await db["matchs"].update_one(
            {
                "mid": match_id
            },{
                "$set": {
                    "players": match["players"]
                }
            }
        )
    
    return match

