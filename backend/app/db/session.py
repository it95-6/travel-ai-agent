from backend.app.core.config import settings


def get_database_url() -> str:
    """Return the database URL placeholder for future SQLite integration."""
    return settings.database_url
