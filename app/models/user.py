import enum
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from app.database import Base


class UserRole(enum.Enum):
    buyer = "buyer"
    seller = "seller"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone_number = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=True)
    role = Column(Enum(UserRole), nullable=False)

    buyer = relationship("Buyer", back_populates="user", uselist=False)
    seller = relationship("Seller", back_populates="user", uselist=False)

