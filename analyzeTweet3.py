import json
import csv
from pymongo import MongoClient
from twython import Twython
from twython import Twython,TwythonError,TwythonRateLimitError
import time
import threading

consumer_key = "RZMGFtwvPzBcCgKdd1giWNTnD"
consumer_secret = "MkO0oNgYsiPomJtmU0nFPuubUm3XQ5O5ZZzbs54UitG8tiZY5F"
access_token = "243047872-DAJCVYpHECs6MBLTx0QoNNRaSyUHrFGXyzVicbpU"
access_token_secret = "OS24CNpPsi5ZcqtnLBagbi0V57wM19WyUwLBwroWc7wuf"

twitter = Twython(consumer_key,consumer_secret,access_token,access_token_secret)

tweetID = '930662550508834816'
file = tweetID +'.txt'
followersFile = tweetID + '.TRT.txt'

tweeter = ""
tweeterID = ""

threads = []

retweeters = []
followers = {}
trt = {}

def lookupTweet(id):
    tweet = twitter.lookup_status(id=tweetID)
    tw = tweet[0]
    global tweeter
    global tweeterID
    tweeter = tw['user']['screen_name']
    tweeterID = tw['user']['id_str']


def fetchRetweeters():
    with open(file) as rts:
        for rt in rts:
            if (len(rt) > 0):
                retweeters.append(rt.strip())


def fetchFollowers(id):
    f = []
    global followers
    next_cursor = -1
    global trt
    while(next_cursor):
        search = twitter.get_followers_ids(user_id=id, count=5000, cursor=next_cursor, stringify_ids=True)
        next_cursor = search["next_cursor"]
        for result in search["ids"]:
            f.append(result)
        time.sleep(60)
    followers[id] = f
    rts = []
    for rt in retweeters:
        if rt in f:
            rts.append(rt)
    trt[id]=rts


if __name__ == '__main__':
    lookupTweet(tweetID)
    fetchRetweeters()
    try:
        fetchFollowers(tweeterID)
    except (TwythonError,TwythonRateLimitError) as te:
        pass
    for rt in retweeters:
        try:
            fetchFollowers(rt)
        except (TwythonError, TwythonRateLimitError) as te:
            pass

with open(followersFile, 'a') as ff:
    print(trt, file=ff)

