import backend.app.db.models  # Ensure ORM models are registered on metadata.
from backend.app.db.base import Base
from backend.app.db.session import engine


def init_db() -> None:
    Base.metadata.create_all(bind=engine)
