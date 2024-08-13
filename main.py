from fastapi import FastAPI

from models import Item


app = FastAPI()

fake_items_db = [
    {"item_name": "Foo"}, 
    {"item_name": "Bar"}, 
    {"item_name": "Baz"}
]


@app.get("/items/")
async def read_item(skip:int=0, limit:int = 10):
    return fake_items_db[skip: skip + limit]

@app.get("/")
async def home():
    return {"mgs": "Test"}


items_list = [] 


@app.post("/items/add")
async def add_item(item: Item):
    items_list.append(item)
    return item