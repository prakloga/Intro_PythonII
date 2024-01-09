import os
import configparser
import requests

# Read credentials.cfg file
config = configparser.ConfigParser()
config.read('credentials.cfg')
GBOOKS_API_KEY = config['API']['GOOGLE_BOOKS']

# REPLACE the following variable with your API Key
API_KEY = GBOOKS_API_KEY
endpoint = "https://www.googleapis.com/books/v1/volumes"

search_term = "The Psychology of Money"
params = {"key": GBOOKS_API_KEY, "q": search_term, "maxResults": 3}
response = requests.get(endpoint, params=params).json()

#for book in response["items"]:
#    title = book["volumeInfo"]["title"]
#    authors = book["volumeInfo"]["authors"]
#    published_date = book["volumeInfo"]["publishedDate"]
#    print(f"{title} | {authors}\n{published_date}\n")

for book in response["items"]:
    volume = book["volumeInfo"]
    title = volume['title']
    published = volume['publishedDate']
    description = volume['description']
    print(f"{title} ({published})\n{description}\n")
