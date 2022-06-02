import uuid
from fastapi import APIRouter, status

from app.database.mongodb import get_db_client
from app.core.config import settings

router = APIRouter(
    prefix="/matchs"
)

@router.get("/new")
async def new_match():
    match_url = "%s/matchs/%s" % (
        settings.PUBLIC_URL,
        uuid.uuid4()
    )

    return {
        "url": match_url
    }
