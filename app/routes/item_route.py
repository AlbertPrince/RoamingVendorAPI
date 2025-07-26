from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.item_schema import ItemCreate, ItemResponse
from app.models.item import Item
from app.models.seller import Seller

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/items/", response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    seller = db.query(Seller).filter(Seller.id == item.seller_id).first()
    if not seller:
        raise HTTPException(status_code=404, detail="Seller not found")
    
    new_item = Item(**item.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@router.get("/items/", response_model=list[ItemResponse])
def get_items(db: Session = Depends(get_db)):
    items = db.query(Item).all()
    if not items:
        raise HTTPException(status_code=404, detail="No items found")
    return items

@router.get("/item/{item_id}", response_model=ItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item