import json
import csv
from pymongo import MongoClient
from twython import Twython,TwythonError,TwythonRateLimitError
import time

consumer_key = "gIituBprWezGxdtubbt65VFBs"
consumer_secret = "cwyummCsSKoNovX4Kr3JZvObXrnlH4Kvf9MDMwWlutXD5zz74E"
access_token = "243047872-MMQkG2uvAoudgqaBCuIYXwT5eiJEICFvL0249zNI"
access_token_secret = "LnRXbg7UV05WCqVOV5O0B6360IDVY1llpXST1nfa7Q4FQ"

twitter = Twython(consumer_key,consumer_secret,access_token,access_token_secret)

temp = ['awscloud','iamdevloper','imoyse','jeffbarr','aws_official','murphdogg11','kubernan','Affgenius','evankirstel','Werner','videopinme','DrDataScientist','compuware']
userLookup = twitter.lookup_user(user_id = temp)

for user in userLookup:
	print(user['screen_name']+"\t"+user['statuses_count'])

