import json
import csv
from pymongo import MongoClient
from twython import Twython
import os.path
import time
import subprocess

consumer_key = "rUzYlA9CStNYhcAvnQd6CLT3H"
consumer_secret = "uIz5mXtq3PzZBnyGOwfsElhP6tOxRU9t8SswTMu6nwMYcNRNf0"
access_token = "243047872-tu4Y0XG1VuDlCmFo4eGdj60AjrmOXedg5YsnrLrE"
access_token_secret = "Nr2baoHT74YqVKfZeES5kzznjd1mcoVLEVk26LBlYi7X3"

twitter = Twython(consumer_key,consumer_secret,access_token,access_token_secret)

followers = {}

followersFile = '/californiaShootingTweets/followers.json'
tweetersFile = '/californiaShootingTweets/UniqueTweeters.txt'

filePath='/californiaShootingTweets/'

with open(followersFile, 'r') as f:
    for line in f:
        if line != "":
            json_acceptable_string = line.replace("'", "\"")
            follow = json.loads(json_acceptable_string)
            keys=follow.keys()
            for key in keys:
                followers[key]=follow[key]

tweeters = []

with open(tweetersFile,'r') as f:
    for line in f:
        if line != " ":
            tweeter=line.rstrip()
            tweeters.append(tweeter)

for tweeter in tweeters:
        fileName=filePath+tweeter+'_FOLLOWERS.txt'
        if os.path.isfile(fileName):
                pass
        else:
                subcommand='../influence_measure/virtual/bin/python GetFollowers.py '+tweeter
                p=subprocess.call(['../influence_measure/virtual/bin/python','GetFollowers.py',tweeter])

