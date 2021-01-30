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

