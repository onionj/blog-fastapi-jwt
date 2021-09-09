from pydantic import BaseSettings


class Settings(BaseSettings):
    secret: str
    algorithm: str

    class Config:
        env_file = ".env"
