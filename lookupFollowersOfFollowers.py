import json
import csv
from pymongo import MongoClient
from twython import Twython
import time

consumer_key = "RZMGFtwvPzBcCgKdd1giWNTnD"
consumer_secret = "MkO0oNgYsiPomJtmU0nFPuubUm3XQ5O5ZZzbs54UitG8tiZY5F"
access_token = "243047872-DAJCVYpHECs6MBLTx0QoNNRaSyUHrFGXyzVicbpU"
access_token_secret = "OS24CNpPsi5ZcqtnLBagbi0V57wM19WyUwLBwroWc7wuf"

file = "SBahnBerlin_follower_ids.txt"

followersFile = "SBahnBerlin_followers_followersCount.txt"

twitter = Twython(consumer_key,consumer_secret,access_token,access_token_secret)


followers = []

with open(file) as f:
	for line in f:
		user_id = line
		followers.append(user_id.rsplit()[0])


i = 0
while(i<len(followers)):
	temp = followers[i:i+100]
	print(temp)
	print(i)
	userLookup = twitter.lookup_user(user_id = temp)
	for user in userLookup:
		with open(followersFile,"a") as fo:
			print(str(user['id_str'])+"\t"+str(user['screen_name'])+"\t"+str(user['followers_count'])+"\t"+str(user['friends_count']),file=fo)
	i = i+100
	time.sleep(5)
