from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    host: str = "127.0.0.1"
    port: int = 8000
    debug: bool = True

    class Config:
        env_file = ".env"


settings = Settings()