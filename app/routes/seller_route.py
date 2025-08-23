from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.seller_schema import SellerCreate, SellerResponse
from app.models.seller import Seller
from app.models.user import User, UserRole
from app.database import SessionLocal

router = APIRouter()

@router.post("", response_model=SellerResponse)
def create_seller(seller_data: SellerCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.phone_number == seller_data.phone_number).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Phone number already exists")

    user = User(
        name=seller_data.name,
        email=seller_data.email,
        phone_number=seller_data.phone_number,
        role=UserRole.seller
    )
    db.add(user)
    db.flush() 

    seller = Seller(
        id=user.id,
        zone=seller_data.zone,
        available_days=seller_data.available_days,
        available_hours=seller_data.available_hours,
        user=user
    )
    db.add(seller)
    db.commit()
    db.refresh(seller)

    return SellerResponse(
        id=seller.id,
        name=user.name,
        email=user.email,
        phone_number=user.phone_number,
        role=user.role,
        zone=seller.zone,
        available_days=seller.available_days,
        available_hours=seller.available_hours
    )



@router.get("", response_model=list[SellerResponse])
def get_sellers(db: Session = Depends(get_db)):
    sellers = db.query(Seller).all()
    if not sellers:
        raise HTTPException(status_code=404, detail="No sellers found")

    return [
        SellerResponse(
            id=s.id,
            name=s.user.name,
            email=s.user.email,
            phone_number=s.user.phone_number,
            role=s.user.role,
            zone=s.zone,
            available_days=s.available_days,
            available_hours=s.available_hours
        )
        for s in sellers
    ]

@router.get("/{seller_id}", response_model=SellerResponse)
def get_seller(seller_id: int, db: Session = Depends(get_db)):
    s = db.query(Seller).filter(Seller.id == seller_id).first()
    if not s:
        raise HTTPException(status_code=404, detail="Seller not found")
    return SellerResponse(
        id=s.id,
        name=s.user.name,
        email=s.user.email,
        phone_number=s.user.phone_number,
        role=s.user.role,
        zone=s.zone,
        available_days=s.available_days,
        available_hours=s.available_hours
    )
