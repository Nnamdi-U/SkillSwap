from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    service_name: str = "identity-profile-service"
    database_url: str = "postgresql+psycopg://skillswap:skillswap@postgres:5432/identity_profiles_db"


settings = Settings()
