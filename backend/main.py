from fastapi import FastAPI, Body
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import List

from database import (
    retrieve_items,
    add_item,
    retrieve_item,
    update_item,
    delete_item
)

app = FastAPI()

# Define the item model
class Item(BaseModel):
    name: str
    description: str

# Routes (CRUD Endpoints)

# Get all items
@app.get("/items", response_description="List all items")
async def get_items():
    items = await retrieve_items()
    return {"items": items}

# Get a single item by ID
@app.get("/items/{id}", response_description="Get a single item")
async def get_item(id: str):
    item = await retrieve_item(id)
    if item:
        return {"item": item}
    return {"message": "Item not found"}

# Create a new item
@app.post("/items", response_description="Add new item")
async def create_item(item: Item = Body(...)):
    item = jsonable_encoder(item)
    new_item = await add_item(item)
    return {"item": new_item}

# Update an item by ID
@app.put("/items/{id}", response_description="Update an item")
async def update_item_data(id: str, item: Item = Body(...)):
    item = {k: v for k, v in item.dict().items() if v is not None}
    updated = await update_item(id, item)
    if updated:
        return {"message": "Item updated successfully"}
    return {"message": "Item not found"}

# Delete an item by ID
@app.delete("/items/{id}", response_description="Delete an item")
async def delete_item_data(id: str):
    deleted = await delete_item(id)
    if deleted:
        return {"message": "Item deleted successfully"}
    return {"message": "Item not found"}

