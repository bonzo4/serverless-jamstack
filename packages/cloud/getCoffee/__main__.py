from pymongo import MongoClient
import os
from bson.json_util import dumps

def main():
    uri = os.environ.get("DATABASE_URL")
    if not uri:
        return {
            "body": {"error": "Database connection string not configured"},
            "statusCode": 500
        }
    
    client = MongoClient(uri)
    
    try:
        db = client["do-coffee"]
        collection = db["available-coffees"]
        
        inventory = list(collection.find({}))
        
        return {
            "body": dumps(inventory),
            "headers": {
                "Content-Type": "application/json"
            }
        }
    except Exception as e:
        print(f"Database error: {str(e)}")
        return {
            "body": {"error": "Failed to retrieve coffee data"},
            "statusCode": 500
        }
    finally:
        client.close()