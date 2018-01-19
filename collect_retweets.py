import tweepy
import json
import csv
from pymongo import MongoClient

consumer_key = "RZMGFtwvPzBcCgKdd1giWNTnD"
consumer_secret = "MkO0oNgYsiPomJtmU0nFPuubUm3XQ5O5ZZzbs54UitG8tiZY5F"
access_token = "243047872-DAJCVYpHECs6MBLTx0QoNNRaSyUHrFGXyzVicbpU"
access_token_secret = "OS24CNpPsi5ZcqtnLBagbi0V57wM19WyUwLBwroWc7wuf"

MONGO_HOST = 'mongodb://localhost/tweets'

def get_retweets(tweetID):
        auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
        auth.set_access_token(access_token,access_token_secret)
        api = tweepy.API(auth)


        client = MongoClient(MONGO_HOST)
        db = client.tweets

        for retweet in tweepy.Cursor(api.retweets(tweetID)):
                print(type(retweet))
                


if __name__ == "__main__":
        get_retweets("927718216926760960")

