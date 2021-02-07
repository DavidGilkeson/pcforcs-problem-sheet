# Author: David Gilkeson

# Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.

# At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.

# Have the program end if the current value is one.

# Please enter a positive integer: 10

# 10 5 16 8 4 2 1

n = int(input("Please enter a positive number: "))    # Takes input from user
  
def collatz(number):                                  # Defines a function called collatz
  
  print(number, end=' ')                              # Prints the first number and end=' ' prints a space and the number in a row
  while number != 1:                                  # While loop will run until the condition is met and then it will break
    if number % 2 == 0:                               # Using the modulo operator(%) to checks if number is even.
      number //= 2                                    # If the number is even, then it divided by 2
      print(number, end=' ')                          # Prints the number with a space and on the same line
    else:
      number = 3 * number + 1                         # Number is multiplied by 3 and 1 is added
      print(number, end=' ')                          # Prints the number with a space and on the same line     
collatz(n)                                            # Function is called  


  # References
  
  # Python Conditions. 2021. Python Conditions. [ONLINE] Available at: https://www.w3schools.com/python/python_conditions.asp. [Accessed 07 February 2021].
  
  # GeeksforGeeks. 2021. Python end parameter in print() - GeeksforGeeks. [ONLINE] Available at: https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/. [Accessed 07 February 2021].
  
  # Python Division - Python Examples. 2021. Python Division - Python Examples. [ONLINE] Available at: https://pythonexamples.org/python-division/. [Accessed 07 February 2021].
  
  # Sweigart, A., 2015.P31-P59, P61-P77  Automate the Boring Stuff with Python. No Starch Press.
