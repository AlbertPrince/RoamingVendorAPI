from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base
from app.models.item_request import ItemRequest
from app.models.user import User

class Buyer(Base):
    __tablename__ = "buyers"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)
    preferences: Mapped[str | None] = mapped_column(String, nullable=True)

    user: Mapped["User"] = relationship(back_populates="buyer")
    item_requests: Mapped[list["ItemRequest"]] = relationship(back_populates="buyer")


    def __repr__(self):
        return f"<Buyer(name={self.user.name}, phone_number={self.user.phone_number})>"