import tweepy
import csv
import json

consumer_key = "ufFsRlxNSLVBiwhab7eD2qnjv"
consumer_secret = "LdEDG8oFJKgMBfTwCmvXz8TfA1dIRHEtECFJNP1GUpP5hCq4Vu"
access_key = "243047872-H5h2lJvE4zBknqb9D06dlqKK2YyAJUu5zp357hSZ"
access_secret = "gv6tDmy6lIrQDZDV7BA1C5LFSp3Z2XcWnDWOIudVZr6X6"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

#allTweets = []

screen_name = "jeffbarr"

def getTweets(screen_name):
	allTweets = []
	newTweets = api.user_timeline(screen_name = screen_name,count=200)
	allTweets.extend(newTweets)
	oldest = allTweets[-1].id - 1
	while len(newTweets) > 0:
		newTweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		allTweets.extend(newTweets)
		oldest = allTweets[-1].id - 1
	tweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in allTweets]
	with open('%s_tweets.csv' % screen_name, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(tweets)

if __name__ == '__main__':
	getTweets(screen_name)
