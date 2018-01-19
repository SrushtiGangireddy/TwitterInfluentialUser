import json
import csv
from pymongo import MongoClient
from twython import Twython
import os.path
import time
import subprocess

consumer_key = "Sk086O2NyEiL51b7kOA1Vur8s"
consumer_secret = "yTZND3JPdGFCQQMF8TPwU0yOS5wiF47XNl2jXUGTCbM3y5Bq1S"
access_token = "243047872-BGdWwZDS4aTxsAXzDWPbuHsd1J0Pus3gmrb55Ift"
access_token_secret = "KYVRB8FvkzZjpDxGyk08oFgRu7ElNMqP7DUfnU8BqLOGo"

twitter = Twython(consumer_key,consumer_secret,access_token,access_token_secret)

followersFile = '/californiaShootingTweets/followers.json'
tweetersFile = '/californiaShootingTweets/UniqueTweeters.txt'

filePath='/californiaShootingTweets/'

tweeters = []

with open(tweetersFile,'r') as f:
    for line in f:
        if line != " ":
            tweeter=line.rstrip()
            tweeters.append(tweeter)
for tweeter in tweeters:
        fileName=filePath+tweeter+'_FOLLOWERS.txt'
        if os.path.isfile(fileName):
                flwrs = []
                try:
                        with open(fileName,'r') as f:
                                for line in f:
                                        flwrs.append(line.rstrip())
                except Exception as e:
                        pass
                followers={}
                followers[tweeter]=flwrs
                print(followers)
                with open(followersFile,'a') as ff:
                        print(followers,file=ff)
