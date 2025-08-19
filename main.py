from fastapi import FastAPI
from app.database import engine
from app.models.seller import Base
from app.routes import item_route, seller_route, item_request_route

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(seller_route.router, prefix="/sellers", tags=["sellers"])
app.include_router(item_route.router, prefix="/items", tags=["items"])
app.include_router(item_request_route.router, prefix="/requests", tags=["requests"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Roaming Market API"}
