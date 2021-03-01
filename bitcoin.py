# Author: David Gilkeson
# 1. Write a program (bitcoin.py) that outputs the current bitcoin price in US Dollars. You may use the code snippet below to get a Dict object that contains the price.
# 2. Extra output all the price in the three currencies, in a neat way.

# I have shown 2 ways of solving the problem
# First way is manually manipulating the data, this is fine as we are only dealing with a small amount of data
# Second way is using a For loop to loop through the JSON and pull out the required data 

import requests
# import json


url = "https://api.coindesk.com/v1/bpi/currentprice.json"         # Code that pulls data from the coin desk api and returns it in JSON 
returnedData = requests.get(url)
bitCoinDict = returnedData.json()
# print(json.dumps(bitCoinDict, indent = 4))                      # This formats the code so it can be easily understood

# usd = bitCoinDict["bpi"]["USD"]["rate"]                         # These variables store the rate of the 3 currencies 
# eur = bitCoinDict["bpi"]["EUR"]["rate"]
# gbp = bitCoinDict["bpi"]["GBP"]["rate"]

# print(f'Bitcoin rate in USD today is ${usd}')                   # Using f strings to format the code and print it to the console
# print(f'Bitcoin rate in EUR today is €{eur}')
# print(f'Bitcoin rate in GBP today is £{gbp}')


for x in bitCoinDict['bpi'].items():                              # This loops through the bpi items
  key, value = x                                                  # The keys and values in x are stored in the key and value variable
  print(f'Bitcoin rate in {key} today is {value["rate"]}')        # This prints the key and value rate to the console

# References

# Stack Overflow. 2021. python - Iterating through a JSON object - Stack Overflow. [ONLINE] Available at: https://stackoverflow.com/questions/2733813/iterating-through-a-json-object. [Accessed 08 February 2021].

# Python JSON. 2021. Python JSON. [ONLINE] Available at: https://www.w3schools.com/python/python_json.asp. [Accessed 03 February 2021].

# Python Dictionaries. 2021. Python Dictionaries. [ONLINE] Available at: https://www.w3schools.com/python/python_dictionaries.asp. [Accessed 03 February 2021].

# www.oreilly.com. 2021. P35. [ONLINE] Available at: https://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf. [Accessed 03 February 2021].

# Stack Overflow. 2021. how to do a dictionary format with f-string in python 3.6? - Stack Overflow. [ONLINE] Available at: https://stackoverflow.com/questions/43488137/how-to-do-a-dictionary-format-with-f-string-in-python-3-6. [Accessed 03 February 2021].