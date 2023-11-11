from fastapi import FastAPI
from utils import get_ips

app = FastAPI()


@app.get("/")
def index():
    return {"Message": "Hello"}


@app.get("/ip")
def get_ip():
    return get_ips()
