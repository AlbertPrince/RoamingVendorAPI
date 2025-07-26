from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.seller_schema import SellerCreate, SellerResponse
from app.models.seller import Seller
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/sellers/", response_model=SellerResponse)
def create_seller(seller: SellerCreate, db: Session = Depends(get_db)):
    existing_seller = db.query(Seller).filter(Seller.phone_number == seller.phone_number).first()
    if existing_seller:
        raise HTTPException(status_code=400, detail="Seller with this phone number already exists")

    db_seller = Seller(**seller.dict())
    db.add(db_seller)
    db.commit()
    db.refresh(db_seller)
    return db_seller

@router.get("/sellers/", response_model=list[SellerResponse])
def get_sellers(db: Session = Depends(get_db)):
    sellers = db.query(Seller).all()
    if not sellers:
        raise HTTPException(status_code=404, detail="No sellers found")
    return sellers

@router.get("/seller/{seller_id}", response_model=SellerResponse)
def get_seller(seller_id: int, db: Session = Depends(get_db)):
    seller = db.query(Seller).filter(Seller.id == seller_id).first()
    if not seller:
        raise HTTPException(status_code=404, detail="Seller not found")
    return seller