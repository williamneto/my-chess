from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

app.include_router(matchs_routes.router)

