from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base
from app.models.user import User

class Seller(Base):
    __tablename__ = "sellers"

    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    zone = Column(String, nullable=True)
    available_days = Column(String, nullable=True)
    available_hours = Column(String, nullable=True)

    user = relationship("User", back_populates="seller")
    items = relationship("Item", back_populates="seller")


    def __repr__(self):
        return f"<Seller(name={self.user.name}, phone_number={self.user.phone_number}, zone={self.zone})>"