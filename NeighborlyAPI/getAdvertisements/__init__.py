import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = os.environ['COSMOSDB_CONN']  # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        database = client[os.environ['MONGODB_NAME']]
        collection = database[os.environ['MONGODB_COL_ADS']]

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

