from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    service_name: str = "session-service"
    database_url: str = "postgresql+psycopg://skillswap:skillswap@postgres:5432/sessions_db"
    identity_service_url: str = "http://identity-profile-service:8000"
    notification_service_url: str = "http://notification-service:8000"


settings = Settings()
