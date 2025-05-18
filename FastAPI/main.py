from fastapi import FastAPI
from enum import Enum

class AvailableCuisines(str, Enum):
    indian = "indian"
    american = "american"
    italian = "italian"

app = FastAPI()

@app.get("/hello/{name}")

async def hello(name):
    return f"Welcome {name}"

@app.get("/")

def read_root():
    return "This is the homepage of the app!"

food= {
    "indian": ["Samosa","Kachori"],
    "italian": ["Pizza","Pasta"],
    "chinese": "Snakes"
}

@app.get("/items/{cuisine}")

async def get_cuisine(cuisine: AvailableCuisines):
    return f"The available {cuisine} cuisines: {food.get(cuisine)}"