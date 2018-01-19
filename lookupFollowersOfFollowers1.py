import json
import csv
from pymongo import MongoClient
from twython import Twython
import time

consumer_key = "mein8I9U85v47SCfYr8sNsPNV"
consumer_secret = "DFtCjot3uGQ5EbGldlU767I86tUkiM1awetBYPJmHURGr5rjxX"
access_token = "243047872-wPIaUE90KFsQR0O6aGR1OFt4eIsteC51B822IWaA"
access_token_secret = "3ULiCm0lWxJFBzxZzLBzhqj1S2SBs3cbtjQ0SfkNLgd2T"

screenName = 'simon_elisha'
fileName = "_FOLLOWERS.txt"
file = screenName+fileName
followersFileName = "_followers_followersCount.txt"
followersFile = screenName+followersFileName


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

