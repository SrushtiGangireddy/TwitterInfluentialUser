import networkx as nx
from operator import itemgetter
import json
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import csv
from pymongo import MongoClient
from twython import Twython
import time

consumer_key = "fwogv9V3hzcAewvhAIN7jjGje"
consumer_secret = "b9IdpwGmFgwyBA7nPSWI4Oe44taGG7H5SxZbBbbmt3uHNYRAvy"
access_token = "243047872-pmjF63VATOG4G5P8NIhCX9y0A8iXvzE8ZVswIBhJ"
access_token_secret = "BMGCj8V3bhUQjm4dcdoLHuTDhv7HSSPwRXMr5v5ajOaME"

twitter = Twython(consumer_key,consumer_secret,access_token,access_token_secret)

G = nx.DiGraph()
color_map = []
tweetId = "912775401084035072"

fileName = '912775401084035072.TRT.txt'
plotName = tweetId + "_Path.png"

tweeter = ""
tweeterID = ""

def lookupTweet(id):
    tweet = twitter.lookup_status(id=id)
    tw = tweet[0]
    global tweeter
    global tweeterID
    tweeter = tw['user']['screen_name']
    tweeterID = tw['user']['id_str']

#counter=1
relationships = {}
with open(fileName,'r') as f:
	for line in f:
		if line != "":
			json_acceptable_string = line.replace("'", "\"")
			trt = json.loads(json_acceptable_string)
			relationships = trt
#print(len(relationships.keys()))
G.add_nodes_from(relationships.keys())
lookupTweet(tweetId)
print(tweeterID)

for key,val in relationships.items():
	if len(val) > 0:
		for value in val:
			G.add_edge(key,value)


#print(G.nodes())
#print(G.edges())

for node in G:
	if node == tweeterID:
		color_map.append('green')
	else:
		color_map.append('orange')

centralityMeasure=nx.betweenness_centrality(G)
#print(centralityMeasure)

nodes = centralityMeasure.items()
sorted(nodes,key=itemgetter(1))
print(nodes)

nx.draw(G,node_color=color_map,node_size=75)
plt.savefig(plotName)
plt.show()
