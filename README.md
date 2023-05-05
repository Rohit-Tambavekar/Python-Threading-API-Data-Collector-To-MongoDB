# Python-Threading-API-Data-Collector-To-MongoDB

## **Introduction**

This README file is for a Python script that fetches data from two different APIs, and saves the data to two different collections in a MongoDB database. The script uses threading to run both API calls in parallel, improving efficiency and reducing overall runtime.

The script connects to a MongoDB instance using a connection string, and then fetches data from two different APIs using requests library. The fetched data is then saved to two different collections in the database. The APIs used in this script are [ISS satellite link](http://api.open-notify.org/iss-now.json) and [Bitstamp link](https://www.bitstamp.net/api/v2/ticker/btcusd/). The former API returns the current location of the International Space Station (ISS), while the latter API returns the current price of Bitcoin in USD.

The script defines a function to fetch data from an API, and the function is run in parallel for both APIs using two separate threads. The thread for each API fetches data from the API, and then saves the data to a collection in the database. The script also defines a variable for the number of retries to make when establishing a connection to an API. If the connection fails, the script retries the connection a specified number of times before giving up.

### **Requirements**

This script requires the following Python packages to be installed:
```
pymongo
requests
pandas
threading
```

It also requires a MongoDB database to be set up and a connection string for the database. The script uses the connection string to connect to the database.

### **Installation and Usage**

To use this script, follow these steps:

Install the required Python packages using pip. For example, run:
```
pip install pymongo 
pip install requests 
pip install pandas
pip install threading.
```
Set up a MongoDB database and obtain the connection string for the database.
Update the mongo_conn_str variable in the script with the connection string for the database.
Run the script using python `Threading json.py`

You can customize the script by changing the number of retries for establishing a connection to an API or changing the URLs for the APIs used in the script. You can also modify the script to fetch data from additional APIs or save the data to additional collections in the database.

### **Functionality**
The script defines a function called `fetch_json_data()` that fetches data from an API and saves it to a collection in a MongoDB database. The function takes two arguments: 
> The URL for the API and the name of the collection to save the data to.

The function makes use of the requests library to establish a connection to the API and fetch the data. If the connection fails, the script retries the connection a specified number of times before giving up. If the connection is successful, the data is saved to the specified collection in the database.

The script uses threading to run two instances of the `fetch_json_data()` function in parallel, one for each API. The script creates two threads, one for each API, and starts the threads. The script then waits for both threads to finish before terminating.

The script also defines variables for the number of retries to make when establishing a connection to an API, and for the names of the collections to save the data to. These variables can be modified to customize the behavior of the script.

### **Conclusion**
This Python script demonstrates how to fetch data from two different APIs and save the data to a MongoDB database using threading. The script uses the requests library to establish connections to the APIs and fetch the data, and the pymongo library to save the data to the database. The use of threading improves the efficiency of the script by allowing the two API calls to be run in parallel. The script can be customized by changing the URLs for the APIs or modifying the code to fetch data from additional APIs or
