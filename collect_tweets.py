from __future__ import print_function
import tweepy
import json
from pymongo import MongoClient

MONGO_HOST = 'mongodb://localhost/aws_tweets'

screen_words = ['#californiashooting','californiashooting']

CONSUMER_KEY = 'l7tPrbAKfXqiZ3uNRMXNe9lqH'
CONSUMER_SECRET = 'oGUvlVmoEksAorBqFcCtpdiRKmpDqH1NWBHJotYSDTCM0E7nQX'
ACCESS_TOKEN = '243047872-cHEedjxmtuBIgGJ33prCent46PqhrHx6T4xyagxI'
ACCESS_TOKEN_SECRET = 'ivYoi7W8w8bxFQNsFs8bCtdKlSW3OV57zzo1pHajAC9je'

class StreamListener(tweepy.StreamListener):
	def on_connect(self):
		print("You are now connected to streaming api")

	def on_error(self,status_code):
		print("An error has occured: "+repr(status_code))
		return False
	
	def on_data(self,data):
		try:
			client = MongoClient(MONGO_HOST)
			db = client.cs
			datajson = json.loads(data)
			created_at = datajson['created_at']
			print("Tweet collected at: "+str(created_at))
			db.csTweets.insert(datajson)
		except Exception as e:
			print(e)

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

listener = StreamListener(api = tweepy.API(wait_on_rate_limit=True))
streamer = tweepy.Stream(auth = auth,listener = listener)
print("collecting tweets with these words: "+str(screen_words))
streamer.filter(track=screen_words)





