from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.buyer import Buyer
from app.models.user import User, UserRole
from app.schemas.buyer_schema import BuyerCreate, BuyerResponse

router = APIRouter(prefix="/buyers", tags=["buyers"])

@router.post("", response_model=BuyerResponse)
def create_buyer(buyer: BuyerCreate, db: Session = Depends(get_db)):
    user = User(
        name=buyer.name,
        email=buyer.email,
        phone_number=buyer.phone_number,
        role=UserRole.buyer
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    buyer = Buyer(user_id=user.id)
    db.add(buyer)
    db.commit()
    db.refresh(buyer)

    return BuyerResponse(
        id=buyer.id,
        name=user.name,
        email=user.email,
        phone_number=user.phone_number,
        role=user.role.value
    )