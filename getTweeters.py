import json
import csv
from pymongo import MongoClient
from twython import Twython, TwythonError
import time
import io
import folium
from geopy import geocoders
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

consumer_key = "RZMGFtwvPzBcCgKdd1giWNTnD"
consumer_secret = "MkO0oNgYsiPomJtmU0nFPuubUm3XQ5O5ZZzbs54UitG8tiZY5F"
access_token = "243047872-DAJCVYpHECs6MBLTx0QoNNRaSyUHrFGXyzVicbpU"
access_token_secret = "OS24CNpPsi5ZcqtnLBagbi0V57wM19WyUwLBwroWc7wuf"

twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)

tweets = '/californiaShootingTweets/CalShootTweets.json'
tweeterFile = '/californiaShootingTweets/Tweeters.txt'

for line in open(tweets,encoding="ISO-8859-1"):
        tweet = json.loads(line)
        tweeter=tweet['Tweeter']
        RTstatus=tweet['retweet']
        if RTstatus is True:
                sourceTweeter=tweet['SourceTweeter']
                with open(tweeterFile,'a') as tf:
                        print(sourceTweeter,file=tf)
                        print(tweeter,file=tf)
        else:
                with open(tweeterFile,'a') as tf:
                        print(tweeter,file=tf)

