from pydantic import BaseModel
from typing import Optional
from app.schemas.user_schema import UserRole

from app.schemas.user_schema import UserBase

class SellerCreate(UserBase):
    name: str
    phone_number: str
    zone: str
    available_days: Optional[str] = None
    available_hours: Optional[str] = None
    role: UserRole = UserRole.seller

class SellerResponse(UserBase):
    id: int
    zone: str
    available_days: Optional[str] = None
    available_hours: Optional[str] = None
    role: UserRole = UserRole.seller

    class Config:
        from_attributes = True