from enum import Enum as PyEnum
from pydantic import BaseModel

class UserRole(str, PyEnum):
    buyer = "buyer"
    seller = "seller"

class UserBase(BaseModel):
    name: str
    email: str
    phone_number: str

class UserCreate(UserBase):
    role: UserRole


class UserResponse(UserBase):
    id: int
    role: UserRole

    class Config:
        from_attributes = True