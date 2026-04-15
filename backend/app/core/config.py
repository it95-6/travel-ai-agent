from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    app_name: str = "Travel AI Agent Backend"
    app_version: str = "0.1.0"
    database_url: str = "sqlite:///./travel_ai.db"


settings = Settings()
