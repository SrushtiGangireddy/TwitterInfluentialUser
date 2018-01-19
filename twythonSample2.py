import json
import csv
from pymongo import MongoClient
from twython import Twython
import time

consumer_key = "Sk086O2NyEiL51b7kOA1Vur8s"
consumer_secret = "yTZND3JPdGFCQQMF8TPwU0yOS5wiF47XNl2jXUGTCbM3y5Bq1S"
access_token = "243047872-BGdWwZDS4aTxsAXzDWPbuHsd1J0Pus3gmrb55Ift"
access_token_secret = "KYVRB8FvkzZjpDxGyk08oFgRu7ElNMqP7DUfnU8BqLOGo"

fileName = "_FOLLOWERS.txt"
userId = '17109147'
twitter = Twython(consumer_key,consumer_secret,access_token,access_token_secret)
userLookup = twitter.lookup_user(user_id=userId)
file = userLookup[0]['screen_name']+fileName
next_cursor = -1

while(next_cursor):
        search = twitter.get_followers_ids(user_id=userId,count=5000,cursor=next_cursor)
        #print(search)
        next_cursor = search["next_cursor"]
        for result in search["ids"]:
                with open(file,"a") as input_file:
                        print(result,file=input_file)

        time.sleep(60)

        #next_cursor = search["next_cursor"]


