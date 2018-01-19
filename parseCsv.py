import csv
tweets = []
screen_name='jeevandongre'
RTFile='retweetCount.txt'
user={}
with open('{}_tweets.csv'.format(screen_name),newline='') as csvfile:
        reader=csv.reader(csvfile,delimiter=',')
        for row in reader:
                tweets.append(row)
RT=0
for tweet in tweets:
        text=tweet[3]
        try:
                RT=RT+int(tweet[1])
        except:
                pass
        tweetID=tweet[0]
user['screen_name']=screen_name
user['Retweet_Count']=RT
with open(RTFile,'a') as f:
	print(user,file=f)

print(RT)

