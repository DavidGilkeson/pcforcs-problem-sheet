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


# names from lab for Week 9
colNames= colNames= (
    'ip',
    'dash1', 
    'userId', 
    'time', 
    'url', 
    'status code', 
    'size of response', 
    'referer', 
    'user agent', 
    'dunno'
)

df = pd.read_csv(filename, sep= ' ', header= None, names=colNames)  
  
print(df)

df['time'] = df['time'].apply(lambda x: re.search('[\w:/]+', x).group())          # Remove brackets from the time

df['time'] = pd.to_datetime(df['time'], format='%d/%b/%Y:%H:%M:%S')               # Convert time to timestamp

df = df.set_index(['time'])                                                       # set the time field as the index
print(df.head())

# 3. Use regular expressions to extract the session id from the URLs and store them in a different column

regex = r'(?<==)\w*\s'                                                            # regex to get after the JSESSIONID=

# function from Week 9 lab 

def getNewValue(x):
  newValue = re.search(regex, x).group().strip()
  return newValue
df['sessionId'] = df['url'].apply(getNewValue)

# 4.  Use groupBy to get the sum of all the data downloaded by each sessionId.


sum_sessions = df[['size of response','sessionId']].groupby(['sessionId']).sum()  # group by sessionId and sum size of response

print(sum_sessions)

#5. Create a plot of this (type of your choice)

sum_sessions['size of response'].plot(kind='bar', color='red')

plt.title("Session ID Data")                                                      # Label the graph
plt.xlabel("SessionID")
plt.ylabel("Data")

plt.grid()                                                                        # Show Grid
plt.show()                                                                        # Show Bar graph


# 6. Extra Work out the amount of data each sessionId downloaded in any given day

daily_downloaded_data = df.groupby(df['sessionId']).resample(rule='D').sum()

print(daily_downloaded_data)


# References

# GeeksforGeeks. 2021. Python | Pandas dataframe.resample() - GeeksforGeeks. [ONLINE] Available at: https://www.geeksforgeeks.org/python-pandas-dataframe-resample/. [Accessed 26 March 2021].

# Matplotlib Bars. 2021. Matplotlib Bars. [ONLINE] Available at: https://www.w3schools.com/python/matplotlib_bars.asp. [Accessed 26 March 2021].

# Pandas DataFrames. 2021. Pandas DataFrames. [ONLINE] Available at: https://www.w3schools.com/python/pandas/pandas_dataframes.asp. [Accessed 22 March 2021].

# Real Python. 2021. Pandas GroupBy: Your Guide to Grouping Data in Python – Real Python. [ONLINE] Available at: https://realpython.com/pandas-groupby/. [Accessed 25 March 2021].

