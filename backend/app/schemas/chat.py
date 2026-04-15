from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, description="User input message.")


class RestaurantCandidate(BaseModel):
    name: str = Field(..., description="Restaurant name.")
    area: str = Field(..., description="Restaurant area.")
    category: str = Field(..., description="Restaurant category.")
    budget: str = Field(..., description="Restaurant budget range.")
    description: str = Field(..., description="Restaurant description.")


class ChatResponse(BaseModel):
    reply: str = Field(..., description="Assistant response message.")
    candidates: list[RestaurantCandidate] = Field(default_factory=list)
