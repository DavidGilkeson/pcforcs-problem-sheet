# Author: David Gilkeson
# Write a program called extract-url.py, that will extract the URLs from an access.log file.

# ie The part of the URL that is stored in the access.log file, complete with the query parameters (I am aware that the host name is not stored in this file, the referring host is)

# The program should store the URLs as strings in a list

# [
# '/cart.do?action=view&itemId=EST-6&productId=SC-MG-G10&JSESSIONID=SD5SL9FF2ADFF4958',
# '/category.screen?categoryId=SHOOTER&JSESSIONID=SD7SL9FF5ADFF5066'
# ]


# Extra (This is extra work for few marks so think about if it is worth doing)
# Store the URLs as a Dictionary object in the list with the resource and parameter names and values separated out eg

# [ 
#    {
#      'resource':'cart.do', 
#      'parameters':{
#          'action':'view',
#          'itemId':'EST-6',
#          'productId':'SC-MG-G10'
#          'JSESSIONID':'SD5SL9FF2ADFF4958'
#      }
#    },
#    #next dictionary object
# ]



import re

filename = "access.log"
dictionary = {}
list_resources = []
count = 0

with open (filename, "r") as logfile:

  for line in logfile:                            # Loops through the log file
    regex = ('(?:(GET|POST) )(\S+)')              # Stores the regex
    url = re.findall(regex, line)[0][1]           # Uses the findall method and stores it in url variable
    list_resources.append(url)                    # Adds url to the list 
          
    resource = re.split("\?", url)[0]             # Splits the url 
    parameters = re.split("\?", url)[1]           # Splits it into parameters

    parameter = re.split("&", parameters)         
    param_dict = {}

    for i in parameter:
      key = re.split('=', i)[0]
      value = re.split('=', i)[1]
      param_dict[key] = value

    dictionary[count] = {'resource': resource, 'parameters': param_dict}
    count += 1

# print(list_resources)

print(dictionary)
    



# References

# GeeksforGeeks. 2021. Python | Check for URL in a String - GeeksforGeeks. [ONLINE] Available at: https://www.geeksforgeeks.org/python-check-url-string/. [Accessed 04 March 2021].

# Python RegEx. 2021. Python RegEx. [ONLINE] Available at: https://www.w3schools.com/python/python_regex.asp. [Accessed 03 March 2021]

# Real Python. 2021. Regular Expressions: Regexes in Python (Part 1) – Real Python. [ONLINE] Available at: https://realpython.com/regex-python/. [Accessed 03 March 2021].