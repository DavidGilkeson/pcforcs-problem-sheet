# Author: David Gilkeson

# 1. Write a program (bitcoin.py) that outputs the current bitcoin price in US Dollars. You may use the code snippet below to get a Dict object that contains the price.
# 2. Extra output all the price in the three currencies, in a neat way.

import requests
# import json

# Code that pulls data from the coin desk api and returns it in JSON 
url = "https://api.coindesk.com/v1/bpi/currentprice.json"
returnedData = requests.get(url)
bitCoinDict = returnedData.json()
# print(json.dumps(bitCoinDict, indent = 4)) # This formats the code so it can be easily understood

# This stores the rate of the 3 currencies
usd = bitCoinDict["bpi"]["USD"]["rate"]
eur = bitCoinDict["bpi"]["EUR"]["rate"]
gbp = bitCoinDict["bpi"]["GBP"]["rate"]

# Using f strings to format the code and print it to the console
print(f'USD rate today is ${usd}')
print(f'EUR rate today is €{eur}')
print(f'GBP rate today is £{gbp}')


# References


# Python JSON. 2021. Python JSON. [ONLINE] Available at: https://www.w3schools.com/python/python_json.asp. [Accessed 03 February 2021].

# Python Dictionaries. 2021. Python Dictionaries. [ONLINE] Available at: https://www.w3schools.com/python/python_dictionaries.asp. [Accessed 03 February 2021].

# Stack Overflow. 2021. how to do a dictionary format with f-string in python 3.6? - Stack Overflow. [ONLINE] Available at: https://stackoverflow.com/questions/43488137/how-to-do-a-dictionary-format-with-f-string-in-python-3-6. [Accessed 03 February 2021].