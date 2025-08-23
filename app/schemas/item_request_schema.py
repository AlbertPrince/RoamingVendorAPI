from pydantic import BaseModel

class ItemRequestBase(BaseModel):
    item_id: int
    buyer_name: str
    contact_info: str
    message: str | None = None

class ItemRequestCreate(ItemRequestBase):
    pass

class ItemRequestResponse(ItemRequestBase):
    id: int

    class Config:
        from_attributes = True