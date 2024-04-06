import pymongo
from datetime import date


client = pymongo.MongoClient("")

db = client["mydatabase"]

calls = db["calls"]

def add_call(where, why):
    today = date.today()
    d2 = today.strftime("%B %d, %Y")

    call_dict = {"where": where, "when": d2, "why": why}

    calls.insert_one(call_dict)

    print("Added call to database!")