from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId  # This imports ObjectId from bson, which comes from pymongo
import os

# Get MongoDB connection URI from environment variable
MONGODB_URI = os.getenv('MONGODB_URI')
client = AsyncIOMotorClient(MONGODB_URI)

db = client['Cyber_Security']  # Database name
collection = db['resources']  # Collection name

# Helper function to convert MongoDB document to a Python dict
# Helper function to convert MongoDB document to a Python dict
def item_helper(item) -> dict:
    return {
        "id": str(item["_id"]),
        "resource_name": item.get("Resource Name", "No Name"),
        "type": item.get("Type", "No Type"),
        "link": item.get("Link", "No Link"),
        "authority": item.get("Authority", "Unknown"),
        "popularity": item.get("Popularity", "Unknown"),
        "category": item.get("Category", "Uncategorized"),
        "author": item.get("Author", "Unknown"),
        "last_updated": item.get("Last Updated", "Unknown"),
        "skill_level": item.get("Skill Level", "Unknown"),
        "access": item.get("Access", "Unknown"),
        "keywords": item.get("Keywords", ""),
        "api_available": item.get("API", "No")
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
        if updated_item.modified_count > 0:
            return True
        return False

# Delete an item by ID
async def delete_item(id: str):
    item = await collection.find_one({"_id": ObjectId(id)})
    if item:
        await collection.delete_one({"_id": ObjectId(id)})
        return True
    return False

# Simple search items with full-text search using MongoDB Atlas Search
async def search_items(query: str):
    pipeline = [
        {
            "$search": {
                "text": {
                    "query": query,
                    "path": ["Resource Name", "Type", "Keywords"]  # Fields to search on
                }
            }
        },
        {
            "$limit": 10  # Limit results to 10
        }
    ]
    
    # Execute the aggregation pipeline
    results = []
    async for item in collection.aggregate(pipeline):
        results.append(item_helper(item))
    
    return results