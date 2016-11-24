import tweepy
from textblob import TextBlob
import configparser

config = configparser.ConfigParser()
config.read('twitterConfig.ini')

# Step 1 - Authenticate
consumer_key = config['twitter API credentials']['consumer_key']
consumer_secret = config['twitter API credentials']['consumer_secret']
access_token = config['twitter API credentials']['access_token']
access_token_secret = config['twitter API credentials']['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Step 2 - Getting a query
# Step 3 - Retrieve Tweets
while True:
    try:
        query = input('Enter a query')
        public_tweets = api.search(query,lang = 'en')
        break
    except tweepy.error.TweepError:
        print('Invalid input. Please try again: ')


# CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
# and label each one as either 'positive' or 'negative', depending on the sentiment
# You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text)

    # Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")