# Author: David Gilkeson

# I want to find which sessionId downloaded the most data

# Read the access.log into a dataframe (see lab)
# Set the date time to be the index (you will need to manipulate this data, see lab)
# Use regular expressions to extract the session id from the URLs and store them in a different column (use the apply function, see lab)
# Use groupBy to get the sum of all the data downloaded by each sessionId.
# Create a plot of this (type of your choice)

# Extra:

# Work out the amount of data each sessionId downloaded in any given day


import pandas as pd
import re
import matplotlib.pyplot as plt

filename = 'access.log'

df = pd.read_table(filename)               # Reads in access log into a dataframe

print(df.head(3))



# References

# Pandas DataFrames. 2021. Pandas DataFrames. [ONLINE] Available at: https://www.w3schools.com/python/pandas/pandas_dataframes.asp. [Accessed 22 March 2021].