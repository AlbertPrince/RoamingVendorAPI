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
    user = User(
        name=buyer_data.name,
        email=buyer_data.email,
        phone_number=buyer_data.phone_number,
        role=UserRole.buyer
    )
    db.add(user)
    db.flush()

    buyer = Buyer(
        id=user.id,
        preferences=buyer_data.preferences,
        user=user
    )
    db.add(buyer)
    db.commit()
    db.refresh(buyer)
    return buyer