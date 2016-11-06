import tweepy
from textblob import TextBlob
import twitterConfig

# Step 1 - Authenticate
consumer_key = twitterConfig.consumer_key
consumer_secret = twitterConfig.consumer_secret
access_token = twitterConfig.access_token
access_token_secret = twitterConfig.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Step 3 - Retrieve Tweets
public_tweets = api.search('MacBook',lang = 'en')

# CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
# and label each one as either 'positive' or 'negative', depending on the sentiment
# You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text)

    # Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")