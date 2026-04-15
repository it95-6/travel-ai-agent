from dataclasses import dataclass, field
from pathlib import Path


def _default_database_url() -> str:
    database_path = Path(__file__).resolve().parents[3] / "travel_ai.db"
    return f"sqlite:///{database_path}"


@dataclass(frozen=True)
class Settings:
    app_name: str = "Travel AI Agent Backend"
    app_version: str = "0.1.0"
    database_url: str = field(default_factory=_default_database_url)


settings = Settings()
