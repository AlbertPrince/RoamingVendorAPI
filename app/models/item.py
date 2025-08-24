from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    seller_id = Column(Integer, ForeignKey("sellers.id"), nullable=False)

    seller = relationship("Seller", back_populates="items")
    requests = relationship("ItemRequest", back_populates="item")

    def __repr__(self):
        return f"<Item(name={self.name}, price={self.price}, seller_id={self.seller_id})>"