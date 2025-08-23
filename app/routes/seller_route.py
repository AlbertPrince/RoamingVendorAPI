from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.seller_schema import SellerCreate, SellerResponse
from app.models.seller import Seller
from app.models.user import User, UserRole
from app.database import SessionLocal

router = APIRouter()

@router.post("/sellers/", response_model=SellerResponse)
def create_seller(seller: SellerCreate, db: Session = Depends(get_db)):
    # existing_seller = db.query(Seller).filter(Seller.phone_number == seller.phone_number).first()
    # if existing_seller:
    #     raise HTTPException(status_code=400, detail="Seller with this phone number already exists")

    # db_seller = Seller(**seller.dict())
    # db.add(db_seller)
    # db.commit()
    # db.refresh(db_seller)
    # return db_seller
    user = User(
        name=seller.name,
        email=seller.email,
        phone_number=seller.phone_number,
        role=UserRole.seller
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    seller_obj = Seller(
        user_id=user.id,
        zone=seller.zone,
        available_days=seller.available_days,
        available_hours=seller.available_hours
    )
    db.add(seller_obj)
    db.commit()
    db.refresh(seller_obj)

    # Return combined response
    return SellerResponse(
        id=seller.id,
        name=user.name,
        email=user.email,
        phone_number=user.phone_number,
        zone=seller_obj.zone,
        available_days=seller_obj.available_days,
        available_hours=seller_obj.available_hours,
        role=user.role.value
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