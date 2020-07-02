
import PySimpleGUI as sg
import tweepy
import json

consumer_key = "nEfVi8N8KBmcmxWC5KqJxdHdc"
consumer_secret = "tK8853ShfWoTaV7smB9X7Mq7RMZmqX3iv7ElmaRXvPT4FMqaqP"
access_key = "1277992408052105217-9bvcOzqKgTx8YJlG2zf3Wtj0ptBoOy"
access_secret = "WgmkljliSqA6qjqKwY6DLPSbkDdQzHmhZFKS9E0m0bEQR"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAMVGFgEAAAAA%2FYJFSdycowTGFf0tcRP9%2BaerZso%3DF3IahdxCBX6nwp6L1Q4bW6ExUlAuLkMKhEXzyYQjQwThyqAcFv"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

'''
places = api.geo_search(query="FRANCE", granularity="country")
place_id = places[0].id
tweets = api.search(q="place:%s" % place_id, count=2)
'''
tweets = api.search(geocode="20.5937,78.9629,3000km", lang="en", count=3)
for tweet in tweets:
    print(tweet)

'''
sg.theme('Dark Blue 3')	# Add a touch of color
# All the stuff inside your window.
layout = [
            [sg.Text('Get some stats about some tweets:')],
            [sg.InputText()],
            [sg.Button('Search by #'),sg.Button('Search by location'),sg.Button('Get current Top Tweets')],
            [sg.Text('No tweets in list')],
            [sg.Button('Exit App')]
        ]


# Create the Window
window = sg.Window('Twitter Stats', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':	# if user closes window or clicks cancel
        break
    if event == 'Search by #':
        print('Search by #: ' + values[0])
    elif event == 'Search by location':
        print('Search by location: ' + values[0])

    elif event == 'Get current Top Tweets':
        print('Get current Top Tweets')


window.close()
'''