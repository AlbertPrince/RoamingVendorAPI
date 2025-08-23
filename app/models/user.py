import enum
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base
from app.models.buyer import Buyer
from app.models.seller import Seller


class UserRole(enum.Enum):
    buyer = "buyer"
    seller = "seller"

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    phone_number: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email: Mapped[str | None] = mapped_column(String, unique=True, nullable=True)
    role: Mapped[UserRole] = mapped_column(Enum(UserRole), nullable=False)

    seller: Mapped["Seller"] = relationship(back_populates="user", uselist=False)
    buyer: Mapped["Buyer"] = relationship(back_populates="user", uselist=False)

