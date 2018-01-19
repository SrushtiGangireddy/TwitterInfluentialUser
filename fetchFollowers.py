import json
import csv
import sys
from pymongo import MongoClient
from twython import Twython
import time

consumer_key = "swA9iwlKhlzH4YfZdKD4z51vT"
consumer_secret = "czKHSroD66p2iLuclqF3XODF1k6ge2gqiY8XEafwdEpKuEwwPK"
access_token = "243047872-0WiqIWIPXygUyy9Wcx55FV668g9rRDDKK9n5MNnF"
access_token_secret = "RZLXKaUaHKr4jHcmzI9GCwZba8qgp5tzhGKfhMR78c0Fq"

fileName = "_FOLLOWERS.txt"
screen_name=sys.argv[1]
twitter = Twython(consumer_key,consumer_secret,access_token,access_token_secret)
userLookup = twitter.lookup_user(screen_name=screen_name)
file = userLookup[0]['screen_name']+fileName
next_cursor = -1

while(next_cursor):
        search = twitter.get_followers_ids(screen_name=screen_name,count=5000,cursor=next_cursor)
        #print(search)
        next_cursor = search["next_cursor"]
        for result in search["ids"]:
                with open(file,"a") as input_file:
                        print(result,file=input_file)

        time.sleep(60)

        #next_cursor = search["next_cursor"]

