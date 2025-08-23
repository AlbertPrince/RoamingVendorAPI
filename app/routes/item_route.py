from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from app.database import get_db
from app.schemas.item_schema import ItemCreate, ItemResponse
from app.models.item import Item
from app.models.seller import Seller

from fastapi import Query
from datetime import time as time_obj

router = APIRouter()

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

@router.get("/search", response_model=list[ItemResponse])
def search_items(
    name: str = Query(None, description="Name of the item to search for"),
    max_price: float = Query(None, description="Maximum price of the item"),
    day: str = Query(None, description="Day of the week to check availability"),
    time: str = Query(None, description="Time to check availability in HH:MM format"),
    db: Session = Depends(get_db)
):
    query = (
        db.query(Item)
        .join(Seller)
        .options(joinedload(Item.seller))
    )

    if name:
        query = query.filter(Item.name.ilike(f"%{name}%"))
    if max_price is not None:
        query = query.filter(Item.price <= max_price)
    if day:
        query = query.filter(Seller.available_days.ilike(f"%{day}%"))

    if not time:
        return query.all()

    try:
        input_time = time_obj.fromisoformat(time)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid time format. Use HH:MM.")

    query = query.filter(Seller.available_hours.isnot(None)).filter(Seller.available_hours != '')

    results = []
    for item in query.all():
        hours_str = item.seller.available_hours
        if not hours_str or "-" not in hours_str:
            continue 

        try:
            start_str, end_str = hours_str.split("-")
            start_time = time_obj.fromisoformat(start_str.strip())
            end_time = time_obj.fromisoformat(end_str.strip())
        except ValueError:
            continue

        if start_time <= input_time <= end_time:
            results.append(item)

    return results
            

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