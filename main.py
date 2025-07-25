from fastapi import FastAPI
from app.database import engine
from app.models.seller import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Roaming Market API"}
