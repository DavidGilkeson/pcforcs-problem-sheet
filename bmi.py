# Author: David Gilkeson
# 1. Write a program that calculates somebody's Body Mass Index (BMI).

# The inputs are the person's height in centimetres and weight in kilograms.
# The output  is their weight divided by their height in metres squared.

# Enter weight: 65
# Enter height: 180
# BMI is 20.06.

weight = int(input("Please enter your weight kilograms: ")) # Takes weight from the user, stores it in a variable called weight and converts it to an integer(whole number)
height = float(input("Please enter your height in cm: ")) # Takes height from the user, stores it in a variable called weight and converts it to a float(decimal number)
height /= 100 # This converts users height input in cm to m

bmi = round(weight/(height**2),2) # The bmi variable stores the users bmi and the round function rounds it to 2 decimal places 
print(f"Your BMI is {bmi}") # This prints out the users BMI using f strings


# References

# Input in Python
# https://www.w3schools.com/python/ref_func_input.asp

# How to take integer input in Python?
# https://www.geeksforgeeks.org/how-to-take-integer-input-in-python/

# How to calculate BMI
# https://www.diabetes.ca/managing-my-diabetes/tools---resources/body-mass-index-(bmi)-calculator#:~:text=Body%20Mass%20Index%20is%20a,most%20adults%2018%2D65%20years

# How to round a number in Python 
# https://www.w3schools.com/python/ref_func_round.asp
