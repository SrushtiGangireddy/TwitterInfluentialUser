import json
import csv
from pymongo import MongoClient
from twython import Twython, TwythonError
import time
import folium
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

consumer_key = "RZMGFtwvPzBcCgKdd1giWNTnD"
consumer_secret = "MkO0oNgYsiPomJtmU0nFPuubUm3XQ5O5ZZzbs54UitG8tiZY5F"
access_token = "243047872-DAJCVYpHECs6MBLTx0QoNNRaSyUHrFGXyzVicbpU"
access_token_secret = "OS24CNpPsi5ZcqtnLBagbi0V57wM19WyUwLBwroWc7wuf"

twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)

trts = '/californiaShootingTweets/RTCount.txt'

geolocator = Nominatim()
sc = {}
tweeters = []
RTcount=[]
locations = []
mapCount = []
with open(trts) as f:
        for line in f:
                if(line):
                        sourceCount = line.strip()
                        jsonSC = json.loads(sourceCount)
                        source=jsonSC['Source']
                        count=jsonSC['Count']
                        sc[source]=count
                        tweeters.append(source)
                        RTcount.append(count)

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
                                mapCount.append(sc[user['screen_name']])
        except (TwythonError, IndexError):
                pass

latLon = []
markCount = []
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
                                markCount.append(mapCount[j])
                except GeocoderTimedOut as e:
                        pass
        j=j+1

map=folium.Map(location=[28,-31],zoom_start=3,tiles="Stamen Terrain")
k=0
for ll in latLon:
        folium.Marker(ll, popup=str(markCount[k]), icon=folium.Icon(icon='message', color='orange')).add_to(map)
        k=k+1

map.save("RetweetCountOnMap.html")

