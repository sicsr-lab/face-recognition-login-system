from pymongo import *
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# Creating a database.
if "db" not in myclient.list_database_names():
    db = myclient["accounts"]

# Creating collection.
if "col" not in db.list_collection_names():
    col = db["users"]

# Block to register user.
def registerUser(*details):
    acc = {"first_name":details[0], "last_name":details[1], "username":details[2], "password":details[3]}
    col.insert_one(acc)

# Block to login.
def loginUser(*details):
    acc = {"username": details[0], "password":details[1]}

    user = col.find_one(acc)

    if user == None:
        return "Sorry we couldn't find your account. Please check credentials."

    else:
        return f"Welcome {user['first_name']} we are glad to have you back."