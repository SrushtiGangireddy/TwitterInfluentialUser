import json
import csv
from pymongo import MongoClient
from twython import Twython, TwythonError
import time
import io
import folium
from geopy import geocoders
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

consumer_key = "RZMGFtwvPzBcCgKdd1giWNTnD"
consumer_secret = "MkO0oNgYsiPomJtmU0nFPuubUm3XQ5O5ZZzbs54UitG8tiZY5F"
access_token = "243047872-DAJCVYpHECs6MBLTx0QoNNRaSyUHrFGXyzVicbpU"
access_token_secret = "OS24CNpPsi5ZcqtnLBagbi0V57wM19WyUwLBwroWc7wuf"

twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)

tweets = '/californiaShootingTweets/Tweets.json'

geolocator = Nominatim()
tweeters = []
retweeters = []
RTcount=[]
locations = []
RTlocations = []
mapCount = []
for line in open(tweets,encoding="ISO-8859-1"):
        tweet = json.loads(line)
        tweeter=tweet['Tweeter']
        RTstatus=tweet['retweet']
        if RTstatus == 'True':
                retweeters.append(tweeter)
        else:
                tweeters.append(tweeter)

i=0
while i < len(tweeters):
        rts = []
        for counter in range(0,100):
                try:
                        rts.append(tweeters[i])
                        i=i+1
                except IndexError:
                        pass

        try:
                users=twitter.lookup_user(screen_name=rts)
                for user in users:
                        if "en" in user['lang']:
                                locations.append(user['location'])
        except (TwythonError, IndexError):
                pass

i=0
while i < len(retweeters):
        rts = []
        for counter in range(0,100):
                try:
                        rts.append(tweeters[i])
                        i=i+1
                except IndexError:
                        pass

        try:
                users=twitter.lookup_user(screen_name=rts)
                for user in users:
                        if "en" in user['lang']:
                                RTlocations.append(user['location'])
        except (TwythonError, IndexError):
                pass
print("Tweeters")
print(tweeters)
print("Retweeters")
print(retweeters)

print("Location of tweeters")
print(locations)

print("Locations of retweeters")
print(RTlocations)


latLon = []
j=0
for location in locations:
        if location:
                try:
                        loc=geolocator.geocode(location)
                        if loc:
                                ll = []
                                ll.append(loc.latitude)
                                ll.append(loc.longitude)
                                latLon.append(ll)
                except (ValueError, GQueryError, GeocoderResultError, GBadKeyError,GeocoderTimedOut):
                        pass
        j=j+1

RTlatLon = []
j=0
for location in locations:
        if location:
                try:
                        loc=geolocator.geocode(location)
                        if loc:
                                ll = []
                                ll.append(loc.latitude)
                                ll.append(loc.longitude)
                                RTlatLon.append(ll)
                except GeocoderTimedOut as e:
                        pass
        j=j+1


map=folium.Map(location=[28,-31],zoom_start=3,tiles="Stamen Terrain")
k=0
for ll in latLon:
        folium.Marker(ll, icon=folium.Icon(icon='message', color='green')).add_to(map)
        k=k+1

k=0
for ll in latLon:
        folium.Marker(ll, icon=folium.Icon(icon='message', color='orange')).add_to(map)
        k=k+1


map.save("tweetsOnMap.html")
