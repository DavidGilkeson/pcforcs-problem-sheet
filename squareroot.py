# Author: David Gilkeson
# Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

# You should create a function called <tt>sqrt</tt> that does this.
# I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x)
# I suggest that you look at the newton method at estimating square roots

# Please enter a positive number: 14.5
# The square root of 14.5 is approx. 3.8.


number = abs(float(input("Please enter a positive number: "))) # Takes positive number from the user, stores it in a variable called number and converts it to a float. abs makes sure it is a positive number.

def sqrt(number):                                              # Defines a function called sqrt that passes in input from user
  x = float(number)                                            # Number is stored and casted to a float
  for i in range(500):                                         # Loops through up to 500
    number = 0.5 * (number + x / number)                       # Logic for getting square root of the input number
    
  return number                                                # Returns number after the approximate square root is calculated

answer = sqrt((number))                                        # Stores function in variable so it can be printed out and called

print(f"The square root of {number} is approx: {answer}")      # Prints out input from user and the number that squareroot of the number




# References

# GeeksforGeeks. 2021. abs() in Python - GeeksforGeeks. [ONLINE] Available at: https://www.geeksforgeeks.org/abs-in-python/. [Accessed 14 February 2021].

# Newton's Square Root Approximation by Ron Kurtus - Succeed in Understanding Algebra: School for Champions. 2021. Newton's Square Root Approximation by Ron Kurtus - Succeed in Understanding Algebra: School for Champions. [ONLINE] Available at: https://www.school-for-champions.com/algebra/square_root_approx.htm. [Accessed 17 February 2021].

# GeeksforGeeks. 2021. Find root of a number using Newton's method - GeeksforGeeks. [ONLINE] Available at: https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/. [Accessed 17 February 2021].

# Sıddık Açıl. 2021. Newton Square Root Method in Python | by Sıddık Açıl | Medium. [ONLINE] Available at: https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d. [Accessed 17 February 2021].