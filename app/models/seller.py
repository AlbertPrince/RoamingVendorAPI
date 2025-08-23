from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Seller(Base):
    __tablename__ = "sellers"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False) 
    zone = Column(String, nullable=False)
    available_days = Column(String, nullable=True) 
    available_hours = Column(String, nullable=True) 
    
    items = relationship("Item", back_populates="seller")
    user = relationship("User", back_populates="seller")


    def __repr__(self):
        return f"<Seller(name={self.user.name}, phone_number={self.user.phone_number}, zone={self.zone})>"