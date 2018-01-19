import tweepy
import json
import csv
from pymongo import MongoClient

consumer_key = "RZMGFtwvPzBcCgKdd1giWNTnD"
consumer_secret = "MkO0oNgYsiPomJtmU0nFPuubUm3XQ5O5ZZzbs54UitG8tiZY5F"
access_token = "243047872-DAJCVYpHECs6MBLTx0QoNNRaSyUHrFGXyzVicbpU"
access_token_secret = "OS24CNpPsi5ZcqtnLBagbi0V57wM19WyUwLBwroWc7wuf"

MONGO_HOST = 'mongodb://localhost/tweets'


def get_all_tweets(userName):
        auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
        auth.set_access_token(access_token,access_token_secret)

        api = tweepy.API(auth)

        TweetDatabase = []

        newTweets = api.user_timeline(screen_name=userName,count=200)

        TweetDatabase.extend(newTweets)

        oldest = TweetDatabase[-1].id - 1

        while len(newTweets) > 0:
                newTweets = api.user_timeline(screen_name=userName,count=200,max_id=oldest)
                TweetDatabase.extend(newTweets)
                oldest = TweetDatabase[-1].id - 1

        try:
                client = MongoClient(MONGO_HOST)
                db = client.tweets
                for tweet in TweetDatabase:
                        datajson = json.loads(tweet)
                        db.awsCloudTweets.insert(datajson)
        except Exception as e:
                print(e)

if __name__ == "__main__":
        get_all_tweets("awscloud")

