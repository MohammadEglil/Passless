import os
import yaml
import json
import pymongo
from pymongo import MongoClient

# Get MongoDB connection URI from environment variable
MONGODB_URI = os.getenv('MONGODB_URI')

# Connect to MongoDB Atlas
client = MongoClient(MONGODB_URI)
db = client['Cyber_Security']  # Database name
collection = db['resources']  # Collection name

def process_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

def push_to_mongo(resource_data):
    # Insert the resource data into MongoDB
    result = collection.insert_one(resource_data)
    print(f"Inserted document with ID: {result.inserted_id}")

def main():
    # Loop through files in the 'resources' directory
    resources_dir = './resources/'  
    for filename in os.listdir(resources_dir):
        if filename.endswith('.yaml'):
            resource_data = process_yaml(os.path.join(resources_dir, filename))
            push_to_mongo(resource_data)


if __name__ == "__main__":
    main()
