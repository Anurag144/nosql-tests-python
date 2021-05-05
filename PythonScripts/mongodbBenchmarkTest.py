import pymongo
import pprint
import json
import pandas as pd
from pymongo import MongoClient
import pql


#------------- Create db connection and create database ----------------------------

def create_connection():
    try:
        conn_string = "mongodb://mongo:secret@localhost:27017/" # <----enter username,pwd,host address and port no accordingly
        myclient = MongoClient(conn_string)
        print("Connected successfully!!!")
        print(myclient)
    except:
        print("Could not connect to MongoDB")

    return myclient

def createDB():
    myclient = create_connection()

    dblist = myclient.list_database_names()
    if "test" in dblist:
        print("The test database exists.")
    else:
        mydb = myclient["test"]

    myclient.close()

def createProfileCollection():
    myclient = create_connection()
    db = myclient.test
    profilesCollection = db["profiles"]
    print(db)
    myclient.close()

def createRelationsCollection():
    myclient = create_connection()
    db = myclient.test
    relationsCollection = db["relations"]
    print(db)
    myclient.close()

def insertIntoProfilesCollection():
    myclient = create_connection()
    db = myclient.test
    profileCol = db.profiles
    # Loading or Opening the json file
    with open('soc-pokec-profiles500.json',errors='ignore') as json_data:
        data = json.load(json_data)
    # Inserting the loaded data in the Collection
    # if JSON contains data more than one entry
    # insert_many is used else inser_one is used
    if isinstance(data, list):
        profileCol.insert_many(data)
    else:
        profileCol.insert_one(data)

    myclient.close()

def insertIntoRelationsCollection():
    myclient = create_connection()
    db = myclient.test
    relationsCol = db.relations
    # Loading or Opening the json file
    with open('soc-pokec-relationship5000.json',errors='ignore') as json_data:
        data = json.load(json_data)
    # Inserting the loaded data in the Collection
    # if JSON contains data more than one entry
    # insert_many is used else inser_one is used
    if isinstance(data, list):
        relationsCol.insert_many(data)
    else:
        relationsCol.insert_one(data)

    myclient.close()

def readProfilesCollection():
    myclient = create_connection()
    db = myclient.test
    mycol = db.profiles
    for x in mycol.find():
        print(x)
    myclient.close()

def readRelationsCollection():
    myclient = create_connection()
    db = myclient.test
    mycol = db.relations
    for x in mycol.find():
        print(x)
    myclient.close()


def dropProfilesCollection():
    myclient = create_connection()
    db = myclient.test
    mycol = db.profiles
    mycol.drop()
    print("profiles connection has been deleted.")
    myclient.close()

def dropRelationsCollection():
    myclient = create_connection()
    db = myclient.test
    mycol = db.relations
    mycol.drop()
    print("relations connection has been deleted.")
    myclient.close()

def singleReadProfilesCollection():
    myclient = create_connection()
    db = myclient.test
    mycol = db.profiles
    x = mycol.find_one()
    print(x)
    myclient.close()

def singleWriteProfilesCollection():
    myclient = create_connection()
    db = myclient.test
    mycol = db.profiles
    with open('soc-pokec-profiles500.json',errors='ignore') as json_data:
        data = json.load(json_data)
    mycol.insert_one(data[400])
    myclient.close()

def aggregationProfiles():
    myclient = create_connection()
    db = myclient.test
    mycol = db.profiles
    aggregate_result = mycol.aggregate([{
                                        "$group":
                                            {
                                                "_id" : "&AGE",
                                                "Aggregate Age" : {"$sum":1}
                                            }
                                        }])

    for i in aggregate_result:
        print(i)
    myclient.close()

def neighborsProfiles():
    myclient = create_connection()
    db = myclient.test
    mycol = db.relations

    record = mycol.find({"_from" : '2'},{"_to": 1}).limit(100)

    for doc in record:
        print(doc)

    myclient.close()



if __name__ == "__main__":
    #createDB()
    #createProfileCollection()
    #createRelationsCollection()
    #insertIntoProfilesCollection()
    #insertIntoRelationsCollection()
    #readProfilesCollection()
    #readRelationsCollection()
    #dropProfilesCollection()
    #dropRelationsCollection()
    #singleReadProfilesCollection()
    #singleWriteProfilesCollection()
    #aggregationProfiles()
    neighborsProfiles()











