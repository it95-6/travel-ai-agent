from typing import List, Literal

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, description="User input message.")


class RecommendationItem(BaseModel):
    category: Literal["travel", "restaurant"] = Field(
        ...,
        description="Recommendation category.",
    )
    title: str = Field(..., description="Recommendation title.")
    reason: str = Field(..., description="Why this recommendation was selected.")


class ChatResponse(BaseModel):
    reply: str = Field(..., description="Assistant response message.")
    recommendations: List[RecommendationItem] = Field(default_factory=list)
