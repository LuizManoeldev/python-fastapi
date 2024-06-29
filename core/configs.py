from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    API_V2_STR: str = '/api/v2'
    DB_URL: str = 'postgresql+asyncpg://postgres:88909506@192.168.1.6:5432/faculdade'
    DBBaseModel: object = declarative_base()
    class Config:
        case_sensitive = True


settings: Settings = Settings()
