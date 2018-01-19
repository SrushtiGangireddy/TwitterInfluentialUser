import json
import csv
from pymongo import MongoClient
from twython import Twython
from twython import TwythonError
from collections import OrderedDict
import time
import operator
from operator import itemgetter

consumer_key = "swA9iwlKhlzH4YfZdKD4z51vT"
consumer_secret = "czKHSroD66p2iLuclqF3XODF1k6ge2gqiY8XEafwdEpKuEwwPK"
access_token = "243047872-0WiqIWIPXygUyy9Wcx55FV668g9rRDDKK9n5MNnF"
access_token_secret = "RZLXKaUaHKr4jHcmzI9GCwZba8qgp5tzhGKfhMR78c0Fq"

twitter = Twython(consumer_key,consumer_secret,access_token,access_token_secret)
tweetCountFile = '/californiaShootingTweets/TweeterFollowerCount.txt'
fCount={}
tweeters = []
with open('UniqueTweeters.txt') as f:
	for line in f:
		user=line.rstrip()
		tweeters.append(user)

i=0
while i < (len(tweeters)):
	if i+100 < len(tweeters):
		j=i+100
	else:
		j=i+(len(tweeters)-i)
	users=tweeters[i:j]
	userLookup = twitter.lookup_user(screen_name=users)
	for ul in userLookup:
		fc=ul['followers_count']
		fCount[ul['screen_name']]=fc
		#print(ul['screen_name']+" "+str(fc))
	i=j

sortedCount=OrderedDict(sorted(fCount.items(),key=itemgetter(1)))
for item in sortedCount:
	jStr=json.dumps({item:fCount[item]})
	with open(tweetCountFile,'a') as tcf:
		print(jStr,file=tcf)

