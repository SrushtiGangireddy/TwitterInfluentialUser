import csv
import json
counter = 0
with open('TweetRetweet.json') as json_file:
	for line in json_file:
		try:
			tweetInfo = json.loads(line)
			counter=counter+1
			print(tweetInfo["sourceTweetID"])
			print(len(tweetInfo["Retweeters"]))
		except:
			pass
#print(counter)
