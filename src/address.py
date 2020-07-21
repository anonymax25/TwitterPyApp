import os
import webbrowser
import tweepy
import folium
import pandas as pd
import random
import yaml

with open("../config.yml", "r") as conf:
    cfg = yaml.load(conf, Loader=yaml.FullLoader)

consumer_key = cfg["consumer_key"]
consumer_secret = cfg["consumer_secret"]
access_key = cfg["access_key"]
access_secret = cfg["access_secret"]
bearer_token = cfg["bearer_token"]
maps_key = cfg["maps_key"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

def getcodeCoordFromAddr(address):
    import googlemaps
    gmaps = googlemaps.Client(maps_key)  # yay la sécurité

    res = gmaps.geocode(address)
    try:
        return res[0]
    except:
        return None


def geoloactedTweets(api, geoInfo, rangeKm, count):
    return api.search(geocode=str(geoInfo['geometry']['location']['lat']) + "," + str(
        geoInfo['geometry']['location']['lng']) + "," + str(rangeKm) + "km", lang="en", count=count)


def getTweetsByAddress(orginAddress, search_range):
    lat = []
    lng = []
    places = []
    values = []
    types = []
    bbox = []
    texts = []

    originGeoInfo = getcodeCoordFromAddr(orginAddress)

    if originGeoInfo != None:

        for tweet in geoloactedTweets(api, originGeoInfo, search_range, 10):

            latVal = None
            lngVal = None
            typesVal = None
            bboxVal = None
            text = "Tweet by : " + tweet._json["user"]["screen_name"] + "               " + tweet._json["text"]

            if tweet._json["coordinates"]:
                typesVal = "coordinates"
                latVal = tweet._json["coordinates"]["coordinates"][1]
                lngVal = tweet._json["coordinates"]["coordinates"][0]

            elif tweet._json["place"]:
                typesVal = "bounding_box"
                bboxVal = tweet._json["place"]["bounding_box"]["coordinates"][0]
            else:
                location = tweet._json['user']['location']
                geoInfo = getcodeCoordFromAddr(location)
                if geoInfo != None:
                    latVal = geoInfo['geometry']['location']['lat'] + random.choice(range(-100, 100)) / 10000
                    lngVal = geoInfo['geometry']['location']['lng'] + random.choice(range(-100, 100)) / 10000

            if typesVal != "bounding_box" and latVal != None and lngVal != None:
                lat.append(latVal)
                lng.append(lngVal)
                places.append(orginAddress)
                values.append(1)
                types.append(typesVal)
                bbox.append(bboxVal)
                texts.append(text)

        # Make a data frame with dots to show on the map
        data = pd.DataFrame({
            'lat': lat,
            'lon': lng,
            'name': places,
            'value': values,
            'type': types,
            'bbox': bbox,
            'text': texts
        })
        data

        print(data)

        # Make an empty map
        m = folium.Map()

        folium.Circle(
            location=(originGeoInfo['geometry']['location']['lat'], originGeoInfo['geometry']['location']['lng']),
            popup='Search point',
            radius=search_range * 1000,
            color='crimson',
            fill=True,
            fill_color='crimson'
        ).add_to(m)

        # I can add marker one by one on the map
        for i in range(0, len(data)):
            if data.iloc[i]['type'] == 'coordinates' or data.iloc[i]['type'] == None:
                folium.Marker(
                    location=[data.iloc[i]['lat'], data.iloc[i]['lon']],
                    popup=data.iloc[i]['text'],
                    color='crimson',
                    fill=True,
                    fill_color='crimson'
                ).add_to(m)
            elif data.iloc[i]['type'] == 'bounding_box':
                folium.Marker(
                    location=(
                        sum([i[1] for i in data.iloc[i]['bbox']]) / len(
                            [i[1] for i in data.iloc[i]['bbox']]) + random.choice(
                            range(-100, 100)) / 10000,
                        sum([i[0] for i in data.iloc[i]['bbox']]) / len(
                            [i[0] for i in data.iloc[i]['bbox']]) + random.choice(
                            range(-100, 100)) / 10000),
                    popup=data.iloc[i]['text'],
                    color='crimson',
                    fill=True,
                    fill_color='crimson'
                ).add_to(m)

        # Save it as html
        m.save('./html/location.html')
        webbrowser.open('file://' + os.path.realpath(os.getcwd() + '/html/user.html'))
