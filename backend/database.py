from motor.motor_asyncio import AsyncIOMotorClient
from bson.objectid import ObjectId
import os

# Get MongoDB connection URI from environment variable
MONGODB_URI = os.getenv('MONGODB_URI')

client = AsyncIOMotorClient(MONGODB_URI)

db = client['Cyber_Security']  # Database name
collection = db['resources']  # Collection name

# Helper function to convert MongoDB document to a Python dict
def item_helper(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "description": item["description"]
    }

# CRUD operations

# Retrieve all items from the database
async def retrieve_items():
    items = []
    async for item in collection.find():
        items.append(item_helper(item))
    return items

# Add a new item to the database
async def add_item(item_data: dict) -> dict:
    item = await collection.insert_one(item_data)
    new_item = await collection.find_one({"_id": item.inserted_id})
    return item_helper(new_item)

# Retrieve a single item with matching ID
async def retrieve_item(id: str) -> dict:
    item = await collection.find_one({"_id": ObjectId(id)})
    if item:
        return item_helper(item)

# Update an item by ID
async def update_item(id: str, data: dict):
    # Return False if no fields to update
    if len(data) < 1:
        return False
    item = await collection.find_one({"_id": ObjectId(id)})
    if item:
        updated_item = await collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_item:
            return True
        return False

# Delete an item by ID
async def delete_item(id: str):
    item = await collection.find_one({"_id": ObjectId(id)})
    if item:
        await collection.delete_one({"_id": ObjectId(id)})
        return True
    return False