#connect to tweepy python library
import tweepy
#import query function from bigquery.py
from bigquery import *
#secrets is just a file containing my twitter account authentication keys
from secrets import *
#connect to twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
#tweet function, takes transaction_count() as a variable and formats the variable into the update status statement
def tweet_transactions():
    total = transaction_count()
    api.update_status('the total number of Bitcoin transactions in the past 24 hours is: {}'.format(total))
#running this function will automatically post to your twitter. consider changing the api.update_status to a print statement for testing purposes
tweet_transactions()
