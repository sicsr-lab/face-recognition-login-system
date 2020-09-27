import pymongo
from passlib.hash import sha256_crypt       # Module to hash passwords.

myclient = pymongo.MongoClient("mongodb://localhost:27017/")        # Creating connection with client.

# Creating a database if not there.
if "db" not in myclient.list_database_names():
    db = myclient["accounts"]

# Creating collection if not there.
if "col" not in db.list_collection_names():
    col = db["users"]

# Block to register user.
def registerUser(*details):
    acc = {"first_name":details[0], "last_name":details[1], "username":details[2], "password":sha256_crypt.hash(details[3])}
    col.insert_one(acc)

# Block to login.
def loginUser(*details):
    acc = {"username": details[0]}
    user = col.find_one(acc)
    
    if user == None:
        return "Sorry we couldn't find your account. Please check credentials."
    elif (sha256_crypt.verify(details[1], user['password']) != True):
        return "Sorry password didn't match"
    else:
        return f"Welcome {user['first_name']}, we are glad to have you back."
