import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union, List


items = [
    {"id": 1, "name": "wine", "description": "french drink", "price": 12.7, "tax": 0.2},
    {"id": 2, "name": "beer", "description": "fresh drink", "price": 2.01},
]


class Item(BaseModel):
    id: int
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = 0.05


app = FastAPI()


@app.get("/items/", response_model=List[Item])
async def read_items():
    return items


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    # Search the item id and return it found
    for item in items:
        if item["id"] == item_id:
            return item


@app.post("/items/{item_id}", response_model=Item)
async def create_item(item_id: int, item: Item):
    items.append(item.dict())
    return item.dict()


@app.put("/items/", response_model=Item)
async def update_item(item: Item):
    # Search the item and update it if found
    for item_id in range(len(items)):
        if items[item_id]["id"] == item.id:
            items[item_id] = item.dict()
            return items[item_id]


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
