from pydantic import BaseModel
from typing import Optional

class SellerCreate(BaseModel):
    name: str
    phone_number: str
    zone: str
    available_days: Optional[str] = None
    available_hours: Optional[str] = None

class SellerResponse(SellerCreate):
    id: int

    class Config:
        orm_mode = True