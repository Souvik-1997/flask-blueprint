# Service for logistics operations

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
                road_collection = db.road
                result = road_collection.find_one({"_id": ObjectId(id)})

                if result["_id"] == ObjectId(id) and result["type"] == type:
                    data = {
                        "id": str(result["_id"]),
                        "name": result["name"],
                        "description": result["description"],
                        "date_created": result["date_created"].strftime(
                            "%b %d %Y, %H:%M:%S"
                        ),
                    }
                else:
                    data = {"error": "Data Not Found!"}

            elif type == "sea":
                sea_collection = db.sea
                result = sea_collection.find_one({"_id": ObjectId(id)})

                if result["_id"] == ObjectId(id) and result["type"] == type:
                    data = {
                        "id": str(result["_id"]),
                        "name": result["name"],
                        "description": result["description"],
                        "date_created": result["date_created"].strftime(
                            "%b %d %Y, %H:%M:%S"
                        ),
                    }
                else:
                    data = {"error": "Data Not Found!"}

            else:
                air_collection = db.air
                result = air_collection.find_one({"_id": ObjectId(id)})

                if result["_id"] == ObjectId(id) and result["type"] == type:
                    data = {
                        "id": str(result["_id"]),
                        "name": result["name"],
                        "description": result["description"],
                        "date_created": result["date_created"].strftime(
                            "%b %d %Y, %H:%M:%S"
                        ),
                    }
                else:
                    data = {"error": "Data Not Found!"}

        except Exception as e:
            data = {"error": str(e)}

        return data

    # def update_data(id, type, req_data):
    #     if type == "road":
    #         road_collection = db.road
    #         result = road_collection.find_one({"_id": ObjectId(id)})
    #         if result["_id"] == ObjectId(id) and result["type"] == "road":
    #             result_data = road_collection.insert_one(
    #                 {
    #                     "type": type,
    #                     "name": req_data["name"],
    #                     "description": req_data["description"],
    #                     "date_created": datetime.utcnow(),
    #                 }
    #             )
    #         return result_data

    #     elif type == "sea":
    #         pass
    #     else:
    #         pass
