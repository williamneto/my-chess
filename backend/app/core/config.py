from pydantic import BaseSettings

class Settings(BaseSettings):
    ENV: str
    HOST: str
    PORT: int
    PUBLIC_URL: str
    MONGO_URI: str
    MONGO_DB_NAME: str
    PUBLIC_URL: str

    class Config:
        env_file = ".env"

settings = Settings()

BOARD = {
    "a1": "t-b", 
    "b1": "c-b", 
    "c1": "b-b", 
    "d1": "r-b", 
    "e1": "d-b", 
    "f1": "b-b", 
    "g1": "c-b", 
    "h1": "t-b", 
    "a2": "p-b", 
    "b2": "p-b", 
    "c2": "p-b", 
    "d2": "p-b", 
    "e2": "p-b", 
    "f2": "p-b", 
    "g2": "p-b", 
    "h2": "p-b", 
    "a3": "", 
    "b3": "", 
    "c3": "", 
    "d3": "", 
    "e3": "", 
    "f3": "", 
    "g3": "", 
    "h3": "", 
    "a4": "", 
    "b4": "", 
    "c4": "", 
    "d4": "", 
    "e4": "", 
    "f4": "", 
    "g4": "", 
    "h4": "", 
    "a5": "", 
    "b5": "", 
    "c5": "", 
    "d5": "", 
    "e5": "", 
    "f5": "", 
    "g5": "", 
    "h5": "", 
    "a6": "", 
    "b6": "", 
    "c6": "", 
    "d6": "", 
    "e6": "", 
    "f6": "", 
    "g6": "", 
    "h6": "", 
    "a7": "p-p", 
    "b7": "p-p", 
    "c7": "p-p", 
    "d7": "p-p", 
    "e7": "p-p", 
    "f7": "p-p", 
    "g7": "p-p", 
    "h7": "p-p",
    "a8": "t-p", 
    "b8": "c-p", 
    "c8": "b-p", 
    "d8": "d-p", 
    "e8": "r-p", 
    "f8": "b-p", 
    "g8": "c-p", 
    "h8": "t-p"
}
