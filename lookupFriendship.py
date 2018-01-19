import json
import csv
from pymongo import MongoClient
from twython import Twython
from twython import Twython,TwythonError,TwythonRateLimitError
import time
import threading

consumer_key = "mIj80gaFYc0jhob7cFx5yCXR7"
consumer_secret = "5qF1SAiuFszHMbXNLhBZkO40bv1GEOz4pyj2xIBimSwaWvriow"
access_token = "243047872-aecR8MeWtZBTaaF8UFXqSWrqHrRdrd14Z3GFffqx"
access_token_secret = "wTS5LBz0fWST7lgo7KRtThgbAntFS0NLOuCN8guBcxcFD"

twitter = Twython(consumer_key,consumer_secret,access_token,access_token_secret)

tweetID = '685195966731816960'
file = tweetID +'.txt'
followersFile = tweetID + '.RTS_FriendshipLookup.txt'

tweeter = ""
tweeterID = ""

threads = []

retweeters = []
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

def lookup(source,target):
    i=0
    follows = []
    while i < len(target):
        j=1
        while j<= 15 & i<len(target):
            friendship = twitter.show_friendship(source_id=source,target_id=target[i])
            if friendship['relationship']['source']['followed_by'] == True:
                follows.append(target[i])
            else:
                pass
            i=i+1
            j=j+1
        time.sleep(900)
    trt[source]=follows
    print(follows)

if __name__ == '__main__':
    lookupTweet(tweetID)
    fetchRetweeters()
    try:
        lookup(tweeterID,retweeters)
    except (TwythonError,TwythonRateLimitError) as te:
        pass

with open(followersFile, 'a') as ff:
    print(trt, file=ff)




