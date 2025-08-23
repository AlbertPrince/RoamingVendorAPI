# app/api/buyers.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User, UserRole
from app.models.buyer import Buyer
from app.schemas.buyer_schema import BuyerCreate, BuyerResponse

router = APIRouter(prefix="/buyers", tags=["buyers"])

@router.post("", response_model=BuyerResponse)
def create_buyer(buyer_data: BuyerCreate, db: Session = Depends(get_db)):
    # 1. Create user
    user = User(
        name=buyer_data.name,
        email=buyer_data.email,
        phone_number=buyer_data.phone_number,
        role=UserRole.buyer
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    # 2. Create buyer profile
    buyer = Buyer(user_id=user.id, preferences=buyer_data.preferences)
    db.add(buyer)
    db.commit()
    db.refresh(buyer)

    # 3. Return response
    return BuyerResponse(
        id=buyer.id,
        name=user.name,
        email=user.email,
        phone_number=user.phone_number,
        role=user.role,
        preferences=buyer.preferences
    )
