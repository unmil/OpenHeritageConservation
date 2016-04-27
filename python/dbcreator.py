from mongoengine import *
from pymongo import MongoClient
import bson.objectid
import bcrypt
import datetime
import argparse
import json
from pprint import pprint
'''Define classes'''


class Wall(Document):
    id = StringField(primary_key=True)
    name = StringField()
    leftWall = StringField()
    rightWall = StringField()
    imageLayersPath = StringField()
    thumbnailPath = StringField()


class User(Document):
    id = StringField(primary_key=True)
    username = StringField()
    password = StringField()
    nickname = StringField()
    email = StringField()
    creationTime = StringField()
    role = StringField()


def fileReader():
    argumentParser = argparse.ArgumentParser(description='please insert parameters')
    argumentParser.add_argument("-w", "--wallData", help="the wall list file name in the default folder")
    argumentParser.add_argument("-u", "--userData", help="the user list file name in the default folder")

    arguments = argumentParser.parse_args()

    if arguments.wallData:

        with open(arguments.wallData) as dataFile:
            wallData = json.load(dataFile)

        wall_init(wallData)



    if arguments.userData:

        with open(arguments.userData) as dataFile:
            userData = json.load(dataFile)

        user_init(userData)



def wall_init(ls):
    dic = {}

    db = connect('myNewDB')
    for obj in ls:
        obj["id"] = str(bson.objectid.ObjectId())
        dic[obj["name"]] = obj["id"]

    for obj in ls:
        obj["leftId"] = dic[obj["leftName"]]
        obj["rightId"] = dic[obj["rightName"]]
        curWall = Wall(name=obj["name"], id=obj["id"], leftWall=obj["leftId"], rightWall=obj["rightId"])
        if (obj["imageLayersPath"] != ""):
            curWall["imageLayersPath"] = obj["imageLayersPath"]
        if (obj["thumbnailPath"] != ""):
            curWall["thumbnailPath"] = obj["thumbnailPath"]
        curWall.save()




def user_init(ls):
    salt = bcrypt.gensalt()

    for sample in ls:
        newUser = User(
            id = str(bson.objectid.ObjectId()),
            username = sample["username"],
            password = bcrypt.hashpw(str(sample["password"]), salt),
            nickname = sample["nickname"],
            email = sample["email"],
            role = sample["role"],
            creationTime = str(datetime.datetime.now())
        )
        newUser.save()

def init_testing():
    # Result Testing
    client = MongoClient()
    db = client.myNewDB
    walls = db.wall.find()
    # for singleWall in walls:
    #    print singleWall

    for singleWall in walls:
        print singleWall['name']
        print "leftWall Name:" + db.wall.find_one({'_id': singleWall['leftWall']})['name']
        print "rightWall Name:" + db.wall.find_one({'_id': singleWall['rightWall']})['name']

    walls = db.wall.find()
    for i in walls:
        print i

    ''' Testing
    if bcrypt.hashpw(str(sample["password"]), str(newUser.password)) == str(newUser.password):
        print("It Matches!")
    else:
        print("It Does not Match :(")

    '''

fileReader()
