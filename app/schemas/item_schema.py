from pydantic import BaseModel
from typing import Optional, List

class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    category: str
    seller_id: int

class ItemResponse(ItemCreate):
    id: int

    class Config:
        orm_mode = True


