#connecting to Bigquery API using your service account

from google.cloud import bigquery
from google.oauth2 import service_account
credentials = service_account.Credentials.from_service_account_file(
    r'PATH TO JSON FILE CONTAINING YOUR GOOGLE CREDENTIALS')
project_id = 'blockchainbot'
client = bigquery.Client(credentials= credentials,project=project_id)

#Querying Database, hash is the unique transaction ID

def transaction_count():
    query1 = '''
    SELECT 
        COUNT(`hash`) as transactions
    FROM
        `bigquery-public-data.crypto_bitcoin.transactions`  
    WHERE
        UNIX_SECONDS(block_timestamp) >= (UNIX_SECONDS(CURRENT_TIMESTAMP()) -86400)
    '''
    #passing query to Bigquery
    query_job = client.query(query1, location= 'US')
    
    #bringing back the result into a variable
    query_result = query_job.result()
    
    #bigquery returns an Array-like object. Specify the first row (0) of column transactions to be returned by the function
    for transactions in query_result:
        return(transactions[0])
