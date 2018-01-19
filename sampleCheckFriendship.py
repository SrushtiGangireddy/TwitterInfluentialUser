from twython import Twython,TwythonError
import datetime

app_key = "l7tPrbAKfXqiZ3uNRMXNe9lqH"
app_secret = "oGUvlVmoEksAorBqFcCtpdiRKmpDqH1NWBHJotYSDTCM0E7nQX"
oauth_token = "243047872-cHEedjxmtuBIgGJ33prCent46PqhrHx6T4xyagxI"
oauth_token_secret = "ivYoi7W8w8bxFQNsFs8bCtdKlSW3OV57zzo1pHajAC9je"

twitter = Twython(app_key,app_secret,oauth_token,oauth_token_secret)

screen_names=["App walker","siro_news","awscloud","Hironobu Ueno"]

relationships = twitter.lookup_friendships(screen_name=["App walker","siro_news","awscloud","Hironobu Ueno"])

for relationship in relationships:
	print(relationship)
