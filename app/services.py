LK# Service for logistics operations

from datetime import datetime
from app import db
from bson import ObjectId


class LogisticsService:
    # Store data
    def store_data(data, collection):
        trans_id = collection.insert_one(
            {
                "type": data["type"],
                "name": data["name"],
                "description": data["description"],
                "date_created": datetime.utcnow(),
            }
        )
        return trans_id

    # Fetch all the objects
    def fetch_all_data():
        air_trans = list(db.air.find())
        road_trans = list(db.road.find())
        sea_trans = list(db.sea.find())

        all_trans = air_trans + road_trans + sea_trans
        # print(list(all_trans))

        trans_data = []

        for trans in all_trans:
            trans["id"] = str(trans["_id"])
            trans["date_created"] = trans["date_created"].strftime("%b %d %Y, %H:%M:%S")
            trans_data.append(trans)

        return trans_data

    # Get data by Id and Type
    def get_data(id, type):
        try:
            if type == "road":
                collection = db.road
            elif type == "sea":
                collection = db.sea
            elif type == "air":
                collection = db.air
            else:
                raise ValueError("Invalid 'type'. Allowed values are 'road', 'sea', or 'air'.")
            
            result = collection.find_one({"_id": ObjectId(id), "type": type})
            if result:
                data = {
                    "id": str(result["_id"]),
                    "type": result["type"],
                    "name": result["name"],
                    "description": result["description"],
                    "date_created": result["date_created"].strftime("%b %d %Y, %H:%M:%S"),
                }
            else:
                data = {"error": "Not Found!"}
            
        except Exception as e:
            data = {"error": str(e)}

        return data

