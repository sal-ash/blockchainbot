# blockchainbot
Twitter bot which posts the daily transaction count of the Bitcoin network. This is done by querying Google Bigquery's live Bitcoin Dataset. The return value of the Query is then passed onto another script which posts the number to twitter on a daily basis. The bot currently runs on AWS Lambda.  

Follow the bot @bot_blockchain on Twitter!
  
The following python libraries are required to run this code:

Tweepy    
Google Cloud  
Google oauth2  
requests
  
Make sure to install these within a virtual environment so as not to mess with your current python setup.  
  
An alternative set up for this bot is provided if you have trouble with the BigQuery dataset. This setup utilises the blockchain.com plaintext query API available [here](https://blockchain.info/q/24hrtransactioncount).  You will need to import the requests python library to run the alternative set up in addition to the tweepy library. As we are no longer using Bigquery neither of the Google libraries is needed.  

To run the code on AWS Lambda just add the below lambda_handler function to the bottom of tweetfunction.py or alternatetweet.py. You will also need to make sure that the dependencies and the scripts are all zipped on the same level directory and uploaded to lambda as a deployment package. it's best to do this on an AWS EC2 instance though it can be done locally if you are running a linux system. Check out [this link](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html) for more details on this.

def lambda_handler(_event_json, _context):
    tweet()

Many thanks to @00jw for his help and support. 
