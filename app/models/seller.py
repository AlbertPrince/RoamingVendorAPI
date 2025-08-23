from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base
from app.models.item import Item
from app.models.user import User

class Seller(Base):
    __tablename__ = "sellers"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    available_days: Mapped[str | None] = mapped_column(String, nullable=True)
    available_hours: Mapped[str | None] = mapped_column(String, nullable=True)

    user: Mapped["User"] = relationship(back_populates="seller")
    items: Mapped[list["Item"]] = relationship(back_populates="seller")


    def __repr__(self):
        return f"<Seller(name={self.user.name}, phone_number={self.user.phone_number}, zone={self.zone})>"