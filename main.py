from fastapi import FastAPI, Path, Query

from typing import Annotated

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

@app.get("/items")
async def get_all_items():
    return items_list


items_list = [] 


@app.post("/items/add")
async def add_item(item: Item):
    items_list.append(item)
    return item


@app.get("/items/{item_id}")
async def get_item(item_id: Annotated[int, Path(title="Id of item to get")],
                   q: Annotated[str | None, Query(alias="item-query")]= None
                   ):
    results = {"item_id": item_id}
    if q:
        return  results.update("q", q)
    return results