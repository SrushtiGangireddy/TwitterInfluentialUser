import tweepy
import time
import json
import csv
from pymongo import MongoClient

consumer_key = "RZMGFtwvPzBcCgKdd1giWNTnD"
consumer_secret = "MkO0oNgYsiPomJtmU0nFPuubUm3XQ5O5ZZzbs54UitG8tiZY5F"
access_token = "243047872-DAJCVYpHECs6MBLTx0QoNNRaSyUHrFGXyzVicbpU"
access_token_secret = "OS24CNpPsi5ZcqtnLBagbi0V57wM19WyUwLBwroWc7wuf"

MONGO_HOST = 'mongodb://localhost/tweets'

client = MongoClient(MONGO_HOST)
db = client.tweets

awscloud_Followers = db.awscloudFollowers


auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

users = tweepy.Cursor(api.followers, screen_name='awscloud', count=200).items()

while True:
    try:
        user = next(users)
    except tweepy.TweepError:
        time.sleep(60*15)
        user = next(users)
    except StopIteration:
        break
    print("@" + user.screen_name)
    awscloud_Followers.insert({'user':user.screen_name})	

