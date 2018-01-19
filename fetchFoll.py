import json
import csv
from pymongo import MongoClient
from twython import Twython
import time

consumer_key = "SVtlNYpzcLs0gczHqX6DABAlV"
consumer_secret = "uj8Wvc6yz6A6vLOhbcU9wviOQgBqnyVQXAEpLsoPhEAEwKLUYA"
access_token = "243047872-QvBw2aygKaZQtyTNZM8o3wn12vU0jZfMgJX3asgy"
access_token_secret = "MTvEwgb5XcgpHJoaiA5ZBo3FodPmLIK5fLQ3Fd7FlGN7c"

fileName = "_FOLLOWERS.txt"
screen_name = 'ecr9495'
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

