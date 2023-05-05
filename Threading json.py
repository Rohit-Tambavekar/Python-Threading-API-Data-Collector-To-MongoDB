pip install pymongo


import pymongo
import time
import json
import pandas as pd
import requests
import threading


# Define the MongoDB connection string
#Enter the database name in <database_name> and password for the database in <password for database>
#do not include the <> just database:password format
mongo_conn_str = "mongodb://<database_name>:<password_for_database>@ac-yaydskh-shard-00-00.dbdtjgb.mongodb.net:27017,ac-yaydskh-shard-00-01.dbdtjgb.mongodb.net:27017,ac-yaydskh-shard-00-02.dbdtjgb.mongodb.net:27017/?ssl=true&replicaSet=atlas-xjikdp-shard-0&authSource=admin&retryWrites=true&w=majority"

# Define the URL for the API request
url1 = "http://api.open-notify.org/iss-now.json"

# Define the second URL for the API request
url2 = "https://www.bitstamp.net/api/v2/ticker/btcusd/"


# Connect to MongoDB and create a connection object
try:
    conn = pymongo.MongoClient(mongo_conn_str)
    print("Connected to MongoDB successfully!")
except pymongo.errors.ConnectionFailure as e:
    print("Could not connect to MongoDB: %s" % e)
    exit()

# Create a variable to hold the satellite data
sat_Data = []
sat_Conn = conn["fetch_data_threading"]


# Define a variable for the number of retries
num_Retries = 3

# Defining a function for threading
def fetch_json_data(url,coll_name):
    start_time=time.time()
    db_Var = sat_Conn[coll_name]
    # Loop through the API request
    for i in range(20):
        # Try to establish a connection to the API
        for j in range(num_Retries):
            try:
                response = requests.get(url)
                response.raise_for_status()
                break
            except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
                print("Connection error: %s" % e)
                if j < num_Retries - 1:
                    print("Retrying...")
                else:
                    print("Max retries exceeded. Exiting...")
                    exit()

        # If the response was successful, insert the data into MongoDB
        if response.status_code == 200:
            data = response.json()
            db_Var.insert_one(data)
            time.sleep(1)
        end_time=time.time()
    elapsed_time=end_time-start_time
    print("Total time taken: ",elapsed_time)
    print("Upload Successful")


# Creating variables for database name. 
# These can also be taken a input during runtime using input() method
collection_name1 = "satellite"
collection_name2 = "stock"


# Create a new thread to fetch JSON data from url1 and save it to collection_name1
sat_Thread = threading.Thread(target=fetch_json_data, args=(url1, collection_name1))
# Start the thread
sat_Thread.start()

# Create a new thread to fetch JSON data from url2 and save it to collection_name2
sto_Thread = threading.Thread(target=fetch_json_data, args=(url2, collection_name2))
# Start the thread
sto_Thread.start()

# Add join() method to wait for threads to finish
sat_Thread.join()
sto_Thread.join()

print("All threads finished")
