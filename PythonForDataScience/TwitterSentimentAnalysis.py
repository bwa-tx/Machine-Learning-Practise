# Twitter Sentiment Analysis using tweepy and textblob dependencies

import tweepy
from textblob import TextBlob
# For consumer keys and api keys goto developers.apps.twitter site 
consumer_key  = 'xxxx'
consumer_secret = 'xxxx'

access_token = 'xxxx'
access_token_secret ='xxxx'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

since_date = "2018-11-3"
until_date = "2018-11-5"

public_tweets = api.search('Virat',count=2,since=since_date,until=until_date)
#print(public_tweets)

for tweet in public_tweets:
	print(tweet.text[1:120])
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	break
	