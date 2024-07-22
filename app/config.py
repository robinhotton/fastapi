from pydantic_settings import BaseSettings
# pip install pydantic-settings

class Settings(BaseSettings):
    mongodb_url: str = "mongodb://localhost:27017"
    database_name: str = "digischool"

settings = Settings()
