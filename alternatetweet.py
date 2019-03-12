#import relevant libraries
import tweepy
import requests
#secrets is a file which holds my twitter authentication keys
from secrets import *
#connect to twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
#the total variable requests the plain text API. This is passed onto the update_status function.
def tweet_transactions():
    total = requests.get('https://blockchain.info/q/24hrtransactioncount')
    api.update_status('the total number of Bitcoin transactions in the past 24 hours is: {}'.format(total.text))
tweet_transactions()
