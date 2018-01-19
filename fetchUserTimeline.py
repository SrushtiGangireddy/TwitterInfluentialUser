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
userTweets=[]
def getTimeline(screen_name):
        allTweets=[]
        newTweets=[]
        oldest=0
        if len(userTweets) == 0:
                newTweets = api.user_timeline(screen_name=screen_name,count=200,trim_user=1,include_rts=False)
                allTweets.extend(newTweets)
                userTweets.extend(newTweets)
                oldest=userTweets[-1].id-1
        else:
                oldest=userTweets[-1].id-1
                newTweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest, trim_user=1,include_rts=False)
                allTweets.extend(newTweets)
                userTweets.extend(newTweets)
                oldest = userTweets[-1].id - 1
        #print(oldest)
        #print(len(newTweets))
        while len(newTweets) > 0:
                newTweets=api.user_timeline(screen_name=screen_name,count=200,max_id=oldest,trim_user=1,include_rts=False)
                userTweets.extend(newTweets)
                allTweets.extend(newTweets)
                oldest=userTweets[-1].id-1

        return allTweets

if __name__ == '__main__':
        screen_name='postmanclient'
        tweets=getTimeline(screen_name)
        tweets=[[tweet.id_str,tweet.retweet_count,tweet.created_at,tweet.text.encode("utf-8")] for tweet in tweets]
        with open('{}_tweets.csv'.format(screen_name), 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["id", "Rt_Count", "created_at", "Text"])
            writer.writerows(tweets)
        #print(len(tweets))
        while len(tweets) > 0:
            tweets = getTimeline(screen_name)
            tweets = [[tweet.id_str, tweet.retweet_count, tweet.created_at, tweet.text.encode("utf-8")] for tweet in tweets]

            with open('{}_tweets.csv'.format(screen_name), 'a') as f:
                writer = csv.writer(f)
                writer.writerows(tweets)


	
