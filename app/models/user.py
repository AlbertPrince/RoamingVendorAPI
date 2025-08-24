from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Column, Integer, String, Enum
from app.database import Base
from enum import Enum as PyEnum
from typing import TYPE_CHECKING




class UserRole(PyEnum):
    buyer = "buyer"
    seller = "seller"
    # admin = "admin"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=True)
    phone_number = Column(String, unique=True, nullable=False)
    role = Column(Enum(UserRole), nullable=False)

    seller = relationship("Seller", back_populates="user", uselist=False)
    buyer = relationship("Buyer", back_populates="user", uselist=False)
