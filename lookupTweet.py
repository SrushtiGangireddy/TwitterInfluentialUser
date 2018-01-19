import json
import csv
from pymongo import MongoClient
from twython import Twython
import time

consumer_key = "ufFsRlxNSLVBiwhab7eD2qnjv"
consumer_secret = "LdEDG8oFJKgMBfTwCmvXz8TfA1dIRHEtECFJNP1GUpP5hCq4Vu"
access_token = "243047872-H5h2lJvE4zBknqb9D06dlqKK2YyAJUu5zp357hSZ"
access_token_secret = "gv6tDmy6lIrQDZDV7BA1C5LFSp3Z2XcWnDWOIudVZr6X6"

twitter = Twython(consumer_key,consumer_secret,access_token,access_token_secret)

tweet = twitter.lookup_status(id="912185400336232449")

tw = tweet[0]

print(tw['user']['id'])
print(tw['user']['screen_name'])
