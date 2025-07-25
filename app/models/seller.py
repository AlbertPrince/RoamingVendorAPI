from sqlalchemy import Column, Integer, String
from app.database import Base

class Seller(Base):
    __tablename__ = "sellers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False, unique=True)
    zone = Column(String, nullable=False)  # e.g., "Madina", "Kaneshie"
    available_days = Column(String, nullable=True)  # comma-separated: "Monday,Tuesday"
    available_hours = Column(String, nullable=True)  # e.g., "08:00-12:00"

    def __repr__(self):
        return f"<Seller(name={self.name}, email={self.email})>"