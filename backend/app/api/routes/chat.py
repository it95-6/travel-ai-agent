from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.db.repositories.restaurant_repository import RestaurantRepository
from backend.app.db.session import get_db
from backend.app.schemas.chat import ChatRequest, ChatResponse
from backend.app.services.chat_service import build_chat_response

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest, db: Session = Depends(get_db)) -> ChatResponse:
    repository = RestaurantRepository(db)
    return build_chat_response(request, repository)
