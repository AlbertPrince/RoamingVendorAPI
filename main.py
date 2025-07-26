from fastapi import FastAPI
from app.database import engine
from app.models.seller import Base
from app.routes import seller_route

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(seller_route.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Roaming Market API"}
