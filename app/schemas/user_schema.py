# from app.models.user import UserRole
from typing import Optional
from pydantic import BaseModel

from enum import Enum

class UserRole(str, Enum):
    buyer = "buyer"
    seller = "seller"


class UserBase(BaseModel):
    name: str
    email: Optional[str] 
    phone_number: str