from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class ItemRequest(Base):
    __tablename__ = "item_requests"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"))
    buyer_name = Column(String, nullable=False)
    contact_info = Column(String, nullable=False)
    message = Column(String, nullable=True)

    item = relationship("Item", back_populates="requests")