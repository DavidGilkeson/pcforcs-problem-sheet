# Author: David Gilkeson
# ok this is a tricky one, but the lab does a bit of this for you.

# (I am not correcting these tasks until the end of the semester)

# I want to find which sessionId downloaded the most data

# Read the access.log into a dataframe (see lab)
# Set the date time to be the index (you will need to manipulate this data, see lab)
# Use regular expressions to extract the session id from the URLs and store them in a different column (use the apply function, see lab)
# Use groupBy to get the sum of all the data downloaded by each sessionId.
# Create a plot of this (type of your choice)

# Extra:

# Work out the amount of data each sessionId downloaded in any given day