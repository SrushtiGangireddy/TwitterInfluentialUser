import json
import csv
from pymongo import MongoClient
from twython import Twython, TwythonError
import time
import folium
from geopy.geocoders import Nominatim
import codecs

geolocator = Nominatim()
locations = []

try:
        f=codecs.open('TweeterLocation.txt',encoding='utf-8')
        for line in f:
                location=line.rstrip()
                locations.append(location)
except UnicodeDecodeError:
        pass

#print(len(locations))

latLon = []
for location in locations:
    if location:
        loc = geolocator.geocode(location)
        if loc:
            ll = []
            ll.append(loc.latitude)
            ll.append(loc.longitude)
            latLon.append(ll)
map = folium.Map(location=[28, -81], zoom_start=3, tiles="Stamen Terrain")

for ll in latLon:
        folium.Marker(ll, popup="Tweet", icon=folium.Icon(icon='message', color='orange')).add_to(map)

map.save("TweetsOnMap.html")

