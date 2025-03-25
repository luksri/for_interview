from fastapi import FastAPI, Depends
from orm_ex import get_db_conn
import httpx

app = FastAPI()

config_val = "some random"

# Function to mock
def get_data():
    return {"message": "Real Data"}

def get_db():
    db = get_db_conn()
    try:
        yield db

    finally:
        db.close()

def get_external_data():
    response = httpx.get("https://api.example.com/data")
    return response.json()
    
class ExternalService:
    def fetch_data(self):
        return "Real Data"


async def get_message():
    return {"msg": "Real Async Data"}

@app.get("/data")
def read_data():
    return get_data()


@app.get("/config")
def read_config():
    return {'config': config_val}


@app.get("/items")
def read_items(db=Depends(get_db)):
    return db
