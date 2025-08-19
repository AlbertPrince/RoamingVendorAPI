from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.item_request import ItemRequest
from app.models.item import Item
from app.schemas.item_request_schema import ItemRequestCreate, ItemRequestResponse

router = APIRouter()

@router.post("", response_model=ItemRequestResponse)
def create_item_request(request: ItemRequestCreate, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == request.item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    new_request = ItemRequest(**request.dict())
    db.add(new_request)
    db.commit()
    db.refresh(new_request)
    return new_request

@router.get("", response_model=list[ItemRequestResponse])
def get_item_requests(db: Session = Depends(get_db)):
    return db.query(ItemRequest).all()