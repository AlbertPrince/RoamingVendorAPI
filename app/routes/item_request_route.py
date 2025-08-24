from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.buyer import Buyer
from app.models.item_request import ItemRequest
from app.models.item import Item
from app.schemas.item_request_schema import ItemRequestCreate, ItemRequestResponse

router = APIRouter()

# @router.post("", response_model=ItemRequestResponse)
# def create_item_request(request: ItemRequestCreate, db: Session = Depends(get_db)):
#     request.validate_buyer()

#     if request.buyer_id:
#         buyer = db.query(Buyer).filter(Buyer.id == request.buyer_id).first()
#         if not buyer:
#             raise HTTPException(status_code=404, detail="Buyer not found")
#         buyer_name = buyer.user.name
#         contact_info = buyer.user.phone_number
#     else:
#         buyer_name = request.buyer_name
#         contact_info = request.contact_info

#     request_data = request.model_dump()
#     request_data["buyer_name"] = buyer_name
#     request_data["contact_info"] = contact_info

#     new_request = ItemRequest(**request_data)
#     db.add(new_request)
#     db.commit()
#     db.refresh(new_request)
#     return new_request

@router.post("", response_model=ItemRequestResponse)
def create_item_request(request: ItemRequestCreate, db: Session = Depends(get_db)):
      buyer = db.query(Buyer).filter(Buyer.id == request.buyer_id).first()
      if not buyer:
          raise HTTPException(status_code=404, detail="Buyer not found")
      
      new_request = ItemRequest(
          item_id=request.item_id,
          buyer_id=request.buyer_id,
          message=request.message,
      )

      db.add(new_request)
      db.commit()
      db.refresh(new_request)
      return new_request

@router.get("", response_model=list[ItemRequestResponse])
def get_item_requests(db: Session = Depends(get_db)):
    return db.query(ItemRequest).all()