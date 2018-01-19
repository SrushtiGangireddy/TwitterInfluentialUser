import json
import csv
from pymongo import MongoClient
from twython import Twython
import time

consumer_key = "Sk086O2NyEiL51b7kOA1Vur8s"
consumer_secret = "yTZND3JPdGFCQQMF8TPwU0yOS5wiF47XNl2jXUGTCbM3y5Bq1S"
access_token = "243047872-BGdWwZDS4aTxsAXzDWPbuHsd1J0Pus3gmrb55Ift"
access_token_secret = "KYVRB8FvkzZjpDxGyk08oFgRu7ElNMqP7DUfnU8BqLOGo"

twitter = Twython(consumer_key,consumer_secret,access_token,access_token_secret)

followers = []

followersDict = {}

followersFile = '/californiaShootingTweets/followers.json'

with open('MuslimIQ_FOLLOWERS.txt') as f:
	for line in f:
		followers.append(line.rstrip())
	followersDict['MuslimIQ']=followers

with open(followersFile,'a') as file:
	print(followersDict,file=file)		


