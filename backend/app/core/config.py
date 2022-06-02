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

