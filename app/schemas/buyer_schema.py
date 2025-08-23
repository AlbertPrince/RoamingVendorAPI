from typing import Optional
from pydantic import BaseModel
from app.schemas.user_schema import UserBase
from app.models.user import UserRole


class BuyerCreate(UserBase):
    phone_number: str
    role: UserRole = UserRole.buyer
    preferences: Optional[str] = None

class BuyerResponse(UserBase):
    id: int
    preferences: Optional[str] = None
    role: UserRole = UserRole.buyer

    class Config:
        from_attributes = True