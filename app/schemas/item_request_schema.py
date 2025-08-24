from typing import Optional
from pydantic import BaseModel

class ItemRequestBase(BaseModel):
    item_id: int
    # buyer_name: Optional[str] = None
    buyer_id: Optional[int] = None
    # contact_info: str
    message: Optional[str] = None

    # def validate_buyer(self):
    #     if not self.buyer_id and not (self.buyer_name and self.contact_info):
    #         raise ValueError("Either buyer_id or both buyer_name and contact_info must be provided")

class ItemRequestCreate(ItemRequestBase):
    pass

class ItemRequestResponse(ItemRequestBase):
    id: int

    class Config:
        from_attributes = True