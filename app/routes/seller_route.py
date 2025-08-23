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
    # 1. Create user
    user = User(
        name=seller_data.name,
        email=seller_data.email,
        phone_number=seller_data.phone_number,
        role=UserRole.seller
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    # 2. Create seller profile
    db_seller = Seller(
        user_id=user.id,
        zone=seller_data.zone,
        available_days=seller_data.available_days,
        available_hours=seller_data.available_hours
    )
    db.add(db_seller)
    db.commit()
    db.refresh(db_seller)

    # 3. Return response
    return SellerResponse(
        id=db_seller.id,
        name=user.name,
        email=user.email,
        phone_number=user.phone_number,
        role=user.role,  
        zone=db_seller.zone,
        available_days=db_seller.available_days,
        available_hours=db_seller.available_hours
    )


@router.get("", response_model=list[SellerResponse])
def get_sellers(db: Session = Depends(get_db)):
    sellers = db.query(Seller).all()
    if not sellers:
        raise HTTPException(status_code=404, detail="No sellers found")
    return sellers

@router.get("/{seller_id}", response_model=SellerResponse)
def get_seller(seller_id: int, db: Session = Depends(get_db)):
    seller = db.query(Seller).filter(Seller.id == seller_id).first()
    if not seller:
        raise HTTPException(status_code=404, detail="Seller not found")
    return seller