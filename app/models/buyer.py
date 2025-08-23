from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.database import Base

class Buyer(Base):
    __tablename_ = "buyers"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    preferences = Column(String, nullable=True)

    user = relationship("User", back_populates="buyer")
    item_requests = relationship("ItemRequest", back_populates="buyer")

    def __repr__(self):
        return f"<Buyer(name={self.user.name}, phone_number={self.user.phone_number})>"