import os
import configparser
import requests

# Read credentials.cfg file
config = configparser.ConfigParser()
config.read('credentials.cfg')
GIPHY_API_KEY = config['API']['GIPHY']


# REPLACE the following variable with your API Key
API_KEY = GIPHY_API_KEY
endpoint = "https://api.giphy.com/v1/gifs/trending"
params = {"api_key": API_KEY, "limit": 3, "rating":"g"}
response = requests.get(endpoint, params=params).json()
for gif in response["data"]:
    title = gif["title"]
    trending_date = gif["trending_datetime"]
    url = gif["url"]
    print(f"{title} | {trending_date}\n{url}\n")
