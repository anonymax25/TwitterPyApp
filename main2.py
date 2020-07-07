import tweepy
from geopy.geocoders import Nominatim
import gmplot




consumer_key = "nEfVi8N8KBmcmxWC5KqJxdHdc"
consumer_secret = "tK8853ShfWoTaV7smB9X7Mq7RMZmqX3iv7ElmaRXvPT4FMqaqP"
access_key = "1277992408052105217-9bvcOzqKgTx8YJlG2zf3Wtj0ptBoOy"
access_secret = "WgmkljliSqA6qjqKwY6DLPSbkDdQzHmhZFKS9E0m0bEQR"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAMVGFgEAAAAA%2FYJFSdycowTGFf0tcRP9%2BaerZso%3DF3IahdxCBX6nwp6L1Q4bW6ExUlAuLkMKhEXzyYQjQwThyqAcFv"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

def geoTweets(count):
    places = api.geo_search(lat='43', long='-75', max_results=1)
    return api.search(q='place:'+places[0].id, count=count)

geolocator = Nominatim(user_agent="pyGeoCode")
coordinates = {'latitude': [], 'longitude': []}

tweets = geoTweets(100)
for count, tweet in enumerate(tweets):
    try:
        location = geolocator.geocode(tweet._json['user']['location'])

        # If coordinates are found for location
        if location:
            coordinates['latitude'].append(location.latitude)
            coordinates['longitude'].append(location.longitude)

    # If too many connection requests
    except:
        pass

# Instantiate and center a GoogleMapPlotter object to show our map
gmap = gmplot.GoogleMapPlotter(30, 0, 3)

# Insert points on the map passing a list of latitudes and longitudes
gmap.heatmap(coordinates['latitude'], coordinates['longitude'], radius=20)

# Save the map to html file
gmap.draw("./html/main2.html")



