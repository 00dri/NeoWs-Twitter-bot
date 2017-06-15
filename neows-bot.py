import urllib2
import json
import tweepy
from datetime import datetime
from credentials import *

current_date = datetime.now().strftime('%Y-%m-%d')

url = "https://api.nasa.gov/neo/rest/v1/feed?start_date=" + current_date
url += "&end_date=" + current_date
url += "&detailed=true&api_key=" + api_key

neows_today = urllib2.urlopen(url).read()

neows = json.loads(neows_today)
neows_count = neows['element_count']
count_potentially_hazardous_asteroids = 0

for i in neows['near_earth_objects'][current_date]:
    if i['is_potentially_hazardous_asteroid'] == 'true':
        count_potentially_hazardous_asteroids += 1

init_tweet = ("Today there will be {x} near earth objects. "
              "{y} of them will be potentially hazardous."
              ).format(x=neows_count, y=count_potentially_hazardous_asteroids)

print(init_tweet)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

api.update_status(init_tweet)