from flask import Flask, request, Response
import pymongo
import json
from bson.objectid import ObjectId
from bson import json_util

app = Flask(__name__)

try:
    mongo = pymongo.MongoClient(
        "mongodb://localhost:27017"
    )
    db = mongo.items
    mongo.server_info()
except Exception as ex:
    print(ex)
    print("Cannot connect to db")


@app.route("/")
def hello_world():
    return "Я родился!"


@app.route('/create_item', methods=["POST"])
def create_item():
    message = "item created"
    id = 0
    status = 200
    try:
        item = request.get_json()
        dbResponce = db.items.insert_one(item)
        id = dbResponce.inserted_id
    except Exception as ex:
        print(ex)
        status = 500
        message = "something is wrong"

    return Response(
        response=json.dumps(
            {"message": f"{message}",
             "id": f"{id}"}
        ),
        status=status,
        mimetype="application/json"
    )


@app.route('/get_item', methods=["POST", "GET"])
def get_item():
    status = 200
    dict_for_return = {}
    try:
        item = request.get_json()

        if "name" in item.keys():
            value = item["name"]
            dict_for_return["name"] = {"$regex": "^" + f"{value}"}

        if "properties" in item.keys():
            key = list(item["properties"][0].keys())[0]
            item_r = item["properties"][0][key]
            dict_for_return["properties"] = {"$all": [{f"{key}": item_r}]}

        arr_for_return = []
        for items in db.items.find(dict_for_return):
            arr_for_return.append(items)
        if not arr_for_return:
            json_for_return = json.dumps({"message": "no items found"})
        else:
            json_for_return = json.dumps({"items": arr_for_return}, default=json_util.default)

    except Exception as ex:
        print(ex)
        status = 500
        json_for_return = json.dumps({"message": "something is wrong"})

    return Response(
        response=json_for_return,
        status=status,
        mimetype="application/json"
    )


@app.route('/id_search', methods = ["POST", "GET"])
def get_details_by_id():
    print(db.items.find({}))
    status = 200
    try:
        item = request.get_json()
        id = item["_id"]
        json_data = db.items.find_one({"_id": ObjectId(f"{id}")})
        properties = json_data["properties"]
        json_return = json.dumps({"properties" : properties})
    except KeyError as ex:
        print(ex)
        status = 400
        json_return = json.dumps({"message" : "bad request"})
    except Exception as ex:
        print(ex)
        status = 500
        json_return = json.dumps({"message": "something is wrong"})

    return Response(
        response=json_return,
        status=status,
        mimetype="application/json"
    )


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
