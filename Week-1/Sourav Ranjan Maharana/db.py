from pymongo import * #This module will help to connect MongoDB with Python

#1. Create the connection
myclient = MongoClient("mongodb://localhost:27017/") #Connection created with client

#2. Create the database
if['db'] not in myclient.list_database_names():
    db=myclient['credentials']

#The following command will help to display the list of databases. Uncomment to see the changes. Uncomment and run, find the output in the terminal.   
for a in myclient.list_database_names():
    print(a)


#3. Create Column
if "col" not in db.list_collection_names():
    col = db["users"]

#The following command will help to display the list of columns/collections in the database. Uncomment and run, find the output in the terminal.
for x in db.list_collection_names():
    print(x)

#4. Add Values