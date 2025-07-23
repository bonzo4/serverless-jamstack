import os

from pymongo import MongoClient

def main(event, context):
    email = event.get("email")
    
    if not email:
        return {
            "body": { "error": "Please provide a valid email." },
            "statusCode": 400
        }
    
    uri = os.environ.get("DATABASE_URL")
    client = MongoClient(uri)
    
    try:
        db = client["do-coffee"]
        collection = db["email-list"]
        collection.insert_one({"subscriber": email})
        return { "ok": True }
    except Exception as e:
        print(e)
        return {
            "body": { "error": "There was a problem adding the email address to the database." },
            "statusCode": 400
        }
    finally:
        client.close()