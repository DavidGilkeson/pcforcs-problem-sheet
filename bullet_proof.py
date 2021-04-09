# Author: David Gilkeson

# Write a (bullet proof) function called averageTo(aList, toIndex)

# The function should take in a list and an index. 

# The function will return the average of the numbers up to and including the toIndex in the aList.

# When I say "bullet proof", I would like the function to always return an integer, even if a error occurs (say return -1), but it will use logging to make a meaningful log warning, for any error that occurs (eg the aList contains an entry that is not a number/ toIndex is not valid, there are many things that could go wrong)

# Write the code to test all the things that could go wrong with this function, and a test to check the function does work.

# The test code can be in the same file or different file.

import logging

logging.basicConfig(filename = './debugging.log', filemode = 'a', level=logging.DEBUG, format='%(asctime)s - %(name)s -  %(levelname)s - %(message)s')                                                    

# logging.basicConfig(level=logging.DEBUG)                          # Debug lets the error print out and used when diagnosing problems

aList = [2,4,7,1,76,23,14,45,99,87,62,33]
toIndex = 13

def check_list(aList):
  
  check_list_type = True
  
  for x in aList:
    if isinstance(x, str):                                        # Checks if x is a string
      print("This list has a string in it")
      check_list_type = False     
  return check_list_type

def check_index(toIndex):
  check_index_type = True
  if type(toIndex) == str:
    print("This cannot be a string")
    check_index_type = False 
  elif type(toIndex) != int:
    print("The value must not be negative")    
    check_index_type = False
  elif toIndex < 0:
    print("The value cannot be negative number")
    check_index_type = False
  elif toIndex > len(aList):
    print("The value is longer than the list ")  
    check_index_type = False
  return check_index_type 
          
def averageTo(aList, toIndex):
  
  sumToIndex = [sum(aList[x : toIndex+1])                         # Got pointed to this code https://www.geeksforgeeks.org/python-sectional-subset-sum-in-list/
   for x in range(0, len(aList), toIndex+1)]
  avgToIndex = sumToIndex[0]/(toIndex+1)  
  return avgToIndex

  # Test Cases
if __name__ == '__main__':
  
  """
  assert averageTo(aList, 6)
  assert averageTo(aList, 0)
  assert averageTo(aList, -10)
  assert averageTo(aList, 11)
  assert averageTo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'a')
  assert averageTo([1, 2, 3, 'hello', 5, 6, 7, 8, 9, 10], 6)
  """
    
  check_list_type = check_list(aList)
  check_index_type = check_index(toIndex)
    
  if check_list_type == True and check_index_type == True:
    print(averageTo(aList, toIndex))
  else:
    print("Invalid Input")  

# References

# GeeksforGeeks. 2021. Python | Sectional subset sum in list - GeeksforGeeks. [ONLINE] Available at: https://www.geeksforgeeks.org/python-sectional-subset-sum-in-list/. [Accessed 03 April 2021].

# logging — Logging facility for Python — Python 3.9.4 documentation. 2021. [ONLINE] Available at: https://docs.python.org/3/library/logging.html#logrecord-attributes. [Accessed 03 April 2021].

# Python Examples of logging.basicConfig. 2021. Python Examples of logging.basicConfig. [ONLINE] Available at: https://www.programcreek.com/python/example/136/logging.basicConfig. [Accessed 01 April 2021].

# Python isinstance() Function. 2021. Python isinstance() Function. [ONLINE] Available at: https://www.w3schools.com/python/ref_func_isinstance.asp. [Accessed 02 April 2021].

# Real Python. 2021. Logging in Python – Real Python. [ONLINE] Available at: https://realpython.com/python-logging/. [Accessed 02 April 2021].

# Real Python. 2021. Python Exceptions: An Introduction – Real Python. [ONLINE] Available at: https://realpython.com/python-exceptions/. [Accessed 02 April 2021].

# YouTube. 2021. Python Tutorial: Logging Basics - Logging to Files, Setting Levels, and Formatting - YouTube. [ONLINE] Available at: https://www.youtube.com/watch?v=-ARI4Cz-awo. [Accessed 02 April 2021].

