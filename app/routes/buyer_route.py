# app/api/buyers.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User, UserRole
from app.models.buyer import Buyer
from app.schemas.buyer_schema import BuyerCreate, BuyerResponse

router = APIRouter(prefix="/buyers", tags=["buyers"])

@router.post("/", response_model=BuyerResponse)
def create_buyer(buyer_data: BuyerCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.phone_number == buyer_data.phone_number).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Phone number already exists")

    user = User(
        name=buyer_data.name,
        email=buyer_data.email,
        phone_number=buyer_data.phone_number,
        role=buyer_data.role
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

    # return BuyerResponse.model_validate(buyer) 
    return BuyerResponse(
        id=int(buyer.id),
        name=user.name,
        email=user.email,
        phone_number=user.phone_number,
        role=user.role,
        preferences=buyer.preferences
    )

@router.get("/", response_model=list[BuyerResponse])
def get_buyers(db: Session = Depends(get_db)):
    buyers = db.query(Buyer).all()
    if not buyers:
        raise HTTPException(status_code=404, detail="No buyers found")

    return [
        BuyerResponse(
            id=b.id,
            name=b.user.name,
            email=b.user.email,
            phone_number=b.user.phone_number,
            role=b.user.role,
            preferences=b.preferences
        )
        for b in buyers
    ]
