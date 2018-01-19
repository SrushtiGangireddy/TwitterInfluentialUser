import json
import csv
from pymongo import MongoClient
import tweepy
import time


consumer_key = "ufFsRlxNSLVBiwhab7eD2qnjv"
consumer_secret = "LdEDG8oFJKgMBfTwCmvXz8TfA1dIRHEtECFJNP1GUpP5hCq4Vu"
access_token = "243047872-H5h2lJvE4zBknqb9D06dlqKK2YyAJUu5zp357hSZ"
access_token_secret = "gv6tDmy6lIrQDZDV7BA1C5LFSp3Z2XcWnDWOIudVZr6X6"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
counter=0
def process_page(page):
	global counter
	counter=counter+len(page)


if __name__ == '__main__':
	screen_name='imoyse'
	for page in tweepy.Cursor(api.user_timeline,screen_name=screen_name,count=200).pages(200):
		print(len(page))
		process_page(page)
	print(counter)
