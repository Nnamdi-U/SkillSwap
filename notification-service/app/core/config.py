from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    service_name: str = "notification-service"
    database_url: str = "postgresql+psycopg://skillswap:skillswap@postgres:5432/notifications_db"


settings = Settings()
