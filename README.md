# blockchainbot
Twitter bot which posts the daily transaction count of the Bitcoin network. This is done by querying Google Bigquery's live Bitcoin Dataset. The return value of the Query is then passed onto another script which posts the number to twitter on a daily basis. The bot currently runs locally but the next stage of this project will be running these scripts from AWS or a similar cloud computing service. Follow the bot @bot_blockchain on Twitter!
  
The following python libraries are required to run this code:   
Tweepy    
Google Cloud  
Google oauth2  
  
Make sure to install these within a virtual environment so as not to mess with your current python setup.  

Many thanks to @00jw for his help and support. 
