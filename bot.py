import tweepy
import corp
import time
from dotenv import load_dotenv
import os

load_dotenv()

while True:
    # authenticate and connect client
    client = tweepy.Client(consumer_key=os.getenv('API_KEY'),
                           consumer_secret=os.getenv('API_SECRET'),
                           access_token=os.getenv('ACCESS_TOKEN'),
                           access_token_secret=os.getenv('ACCESS_SECRET'),
                           wait_on_rate_limit=True)

    # create simple query for recent tweet search
    query = 'from:cnnbrk'
    tweets = client.search_recent_tweets(query=query,
                                         max_results=50,
                                         user_auth=True)

    tweet_list = []
    for tweet in tweets.data:
        tweet_list.append(tweet.text)

    # create corpus of words from the matching tweets and generate headline(s)
    new_corpus = corp.create_corpus(tweet_list)
    new_tweet = corp.generate_tweet(new_corpus)

    # tweet the new message
    client.create_tweet(text=new_tweet, user_auth=True)

    time.sleep(300)
