import sys
import requests
import json
# Cole Rogers cbr9yef
# read in stocks as command line arguments
stocks = sys.argv[1:]


# You need to put the api key in an otherwise empty file called keyfile.txt
# This is so it works with the gitignore
# alternativly just comment this out and replace api_key with a key in 
# the headers section
try:
    keyfile = open('keyfile.txt', 'r')
    api_key = keyfile.readline().strip()
except:
    print("Put your api key in a file titled 'keyfile.txt' to continue")
    sys.exit()

url = "https://yfapi.net/v6/finance/quote"
# generate querrystring
querystring = {"symbols":",".join(str(stock) for stock in stocks)}

headers = {
    'x-api-key': api_key,
    }

response = requests.request("GET", url, headers=headers, params=querystring)
jticker = response.json()
for i in range(0, len(stocks)):
    try:
        name = jticker["quoteResponse"]["result"][i]["longName"]
        price = jticker["quoteResponse"]["result"][i]["regularMarketPrice"]
        print(name + ": " + str(price))
    except:
        print("Error: stock " + stocks[i] + " can not be found")