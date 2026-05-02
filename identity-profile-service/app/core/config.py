from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    service_name: str = "identity-profile-service"
    database_url: str = "postgresql+psycopg://skillswap:skillswap@postgres:5432/identity_profiles_db"
    jwt_secret_key: str = "change-me-in-local-env"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7
    mfa_issuer_name: str = "SkillSwap"


settings = Settings()
