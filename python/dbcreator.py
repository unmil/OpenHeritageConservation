from mongoengine import *
from pymongo import MongoClient
import bson.objectid
import bcrypt
import datetime
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


def init():
    ls = [
        {
            "name": "A",
            "leftName": "B",
            "rightName": "R",
            "imageLayersPath": "A-Bay1south/A-bay1south_img",
            "thumbnailPath": "A.jpg"
        },
        {
            "name": "B",
            "leftName": "C",
            "rightName": "A",
            "imageLayersPath": "B-Bay2_South/B-Bay2SouthZoomify_img",
            "thumbnailPath": "B.jpg"
        },
        {
            "name": "C",
            "leftName": "D",
            "rightName": "B",
            "imageLayersPath": "C-Bay3south/C-Bay3south_img",
            "thumbnailPath": "C.jpg"
        },
        {
            "name": "D",
            "leftName": "E",
            "rightName": "C",
            "imageLayersPath": "D-Bay4_South",
            "thumbnailPath": "placeholder-thumbnail.jpg"
        },
        {
            "name": "E",
            "leftName": "F",
            "rightName": "D",
            "imageLayersPath": "E-TranseptSouthwest",
            "thumbnailPath": "placeholder-thumbnail.jpg"
        },
        {
            "name": "F",
            "leftName": "G",
            "rightName": "E",
            "imageLayersPath": "F-TranseptSouth/F-TranceptSouth_img",
            "thumbnailPath": "F.jpg"
        },
        {
            "name": "G",
            "leftName": "H",
            "rightName": "F",
            "imageLayersPath": "",
            "thumbnailPath": "placeholder-thumbnail.jpg"
        },
        {
            "name": "H",
            "leftName": "I",
            "rightName": "G",
            "imageLayersPath": "",
            "thumbnailPath": "placeholder-thumbnail.jpg"
        },
        {
            "name": "I",
            "leftName": "J",
            "rightName": "H",
            "imageLayersPath": "",
            "thumbnailPath": "placeholder-thumbnail.jpg"
        },
        {
            "name": "J",
            "leftName": "I",
            "rightName": "K",
            "imageLayersPath": "",
            "thumbnailPath": "placeholder-thumbnail.jpg"
        },
        {
            "name": "K",
            "leftName": "J",
            "rightName": "L",
            "imageLayersPath": "",
            "thumbnailPath": "placeholder-thumbnail.jpg"
        },
        {
            "name": "L",
            "leftName": "M",
            "rightName": "K",
            "imageLayersPath": "",
            "thumbnailPath": "placeholder-thumbnail.jpg"
        },
        {
            "name": "M",
            "leftName": "N",
            "rightName": "L",
            "imageLayersPath": "",
            "thumbnailPath": "placeholder-thumbnail.jpg"
        },
        {
            "name": "N",
            "leftName": "O",
            "rightName": "M",
            "imageLayersPath": "",
            "thumbnailPath": "placeholder-thumbnail.jpg"
        },
        {
            "name": "O",
            "leftName": "P",
            "rightName": "N",
            "imageLayersPath": "",
            "thumbnailPath": "placeholder-thumbnail.jpg"
        },
        {
            "name": "P",
            "leftName": "Q",
            "rightName": "O",
            "imageLayersPath": "",
            "thumbnailPath": "placeholder-thumbnail.jpg"
        },
        {
            "name": "Q",
            "leftName": "R",
            "rightName": "P",
            "imageLayersPath": "",
            "thumbnailPath": "placeholder-thumbnail.jpg"
        },
        {
            "name": "R",
            "leftName": "A",
            "rightName": "Q",
            "imageLayersPath": "",
            "thumbnailPath": "placeholder-thumbnail.jpg"
        }
    ]

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

def user_add():
    sample = {
        "username":"admin",
        "password":"admin",
        "nickname":"admin",
        "email":"admin@admin.com",
        "role":"conservator"
    }
    salt = bcrypt.gensalt()

    newUser = User(
        username = sample["username"],
        password = bcrypt.hashpw(sample["password"], salt),
        nickname = sample["nickname"],
        email = sample["email"],
        role = sample["role"],
        creationTime = str(datetime.datetime.now())
    )
    ''' Testing
    if bcrypt.hashpw(str(sample["password"]), str(newUser.password)) == str(newUser.password):
        print("It Matches!")
    else:
        print("It Does not Match :(")

    '''



#init()
#init_testing()
user_add()