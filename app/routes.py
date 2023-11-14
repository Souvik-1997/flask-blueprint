from ast import dump
from json import dumps
from flask import request, Blueprint, json, make_response
from app import db
from app.schemas import transports_schema
from cerberus import Validator
from app.services import LogisticsService

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    trans_data = LogisticsService.fetch_all_data()
    json_data = dumps(trans_data, default=str)

    response = make_response(json_data)
    response.headers["Content-Type"] = "application/json"

    response_data = {
        "message": "The list has been fetched successfully.",
        "success": True,
        "result": {"data": response},
    }

    return response_data, 200


@bp.route("/insert_data/", methods=["GET", "POST"])
def insert_data():
    if request.method == "POST":
        req_data = request.get_json()
        trans_type = req_data["type"]

        v_trans = Validator(transports_schema)

        try:
            if v_trans.validate(req_data):
                print("Data is valid")
                if trans_type == "road":
                    road_collection = db.road
                    insert_id = LogisticsService.store_data(req_data, road_collection)

                elif trans_type == "sea":
                    sea_collection = db.sea
                    insert_id = LogisticsService.store_data(req_data, sea_collection)
                    print(insert_id)

                else:
                    air_collection = db.air
                    insert_id = LogisticsService.store_data(req_data, air_collection)

            else:
                print("Data is invalid", v_trans.errors)
        except Exception as e:
            print(e)

    response_data = {
        "message": "The data has been stored successfully.",
        "success": True,
        "result": {"data": ""},
    }

    return response_data, 200


@bp.route("/edit/<id>/<type>", methods=["GET"])
def edit_data(id, type):
    result = LogisticsService.get_data(id, type)
    json_data = dumps(result, default=str)

    response_data = {
        "message": "The data has been fetched successfully.",
        "success": True,
        "result": {"data": json_data},
    }
    return response_data, 200
    
    
