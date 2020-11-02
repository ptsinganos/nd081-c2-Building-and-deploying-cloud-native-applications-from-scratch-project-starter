import azure.functions as func
import pymongo
from bson.objectid import ObjectId

def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')
    request = req.get_json()

    if request:
        try:
            url = "mongodb://db-ae50100a-d375-47d4-b021-5db05c787e89:GdaGuRyTMmT1foEHy8uBUknN3EPA0dorhCw8j9MmjAaHa9gqrzgKidmv4SKPrjDin5hJIbMbpB8cnh3sBJxevw==@db-ae50100a-d375-47d4-b021-5db05c787e89.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"  # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client['azure']
            collection = database['advertisements']
            
            filter_query = {'_id': ObjectId(id)}
            update_query = {"$set": eval(request)}
            rec_id1 = collection.update_one(filter_query, update_query)
            return func.HttpResponse(status_code=200)
        except:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)
    else:
        return func.HttpResponse('Please pass name in the body', status_code=400)

