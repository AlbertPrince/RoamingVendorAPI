from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base
from app.models.item_request import ItemRequest
from app.models.seller import Seller

class Item(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str | None] = mapped_column(String, nullable=True)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    seller_id: Mapped[int] = mapped_column(ForeignKey("sellers.id"), nullable=False)

    seller: Mapped["Seller"] = relationship(back_populates="items")
    requests: Mapped[list["ItemRequest"]] = relationship(back_populates="item")

    def __repr__(self):
        return f"<Item(name={self.name}, price={self.price}, seller_id={self.seller_id})>"