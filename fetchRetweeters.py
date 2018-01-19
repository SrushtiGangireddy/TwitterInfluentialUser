import json
import csv
from pymongo import MongoClient
from twython import Twython
import time

consumer_key = "RZMGFtwvPzBcCgKdd1giWNTnD"
consumer_secret = "MkO0oNgYsiPomJtmU0nFPuubUm3XQ5O5ZZzbs54UitG8tiZY5F"
access_token = "243047872-DAJCVYpHECs6MBLTx0QoNNRaSyUHrFGXyzVicbpU"
access_token_secret = "OS24CNpPsi5ZcqtnLBagbi0V57wM19WyUwLBwroWc7wuf"

tweetID = "929981114248130560"
filename = "_Retweeter_ids.txt"
file = tweetID+filename

twitter = Twython(consumer_key,consumer_secret,access_token,access_token_secret)

retweeters = twitter.get_retweeters_ids(id=tweetID,stringify_ids=True)
next_cursor = -1

while(next_cursor):
	search = twitter.get_retweeters_ids(id=tweetID,count=100,cursor=next_cursor,stringify_ids=True)
	next_cursor = search["next_cursor"]
	for result in search["ids"]:
		with open(file,"a") as tweeters_file:
			print(result,file=tweeters_file)
	time.sleep(60)

