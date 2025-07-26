from sqlalchemy import Column, Integer, String
from app.database import Base

class Seller(Base):
    __tablename__ = "sellers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False, unique=True)
    zone = Column(String, nullable=False)  
    available_days = Column(String, nullable=True) 
    available_hours = Column(String, nullable=True) 


    def __repr__(self):
        return f"<Seller(name={self.name}, phone_number={self.phone_number}, zone={self.zone})>"