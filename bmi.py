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

# Python input() Function. 2021. Python input() Function. [ONLINE] Available at: https://www.w3schools.com/python/ref_func_input.asp. [Accessed 27 January 2021].

# GeeksforGeeks. 2021. How to take integer input in Python? - GeeksforGeeks. [ONLINE] Available at: https://www.geeksforgeeks.org/how-to-take-integer-input-in-python/. [Accessed 27 January 2021].

# DiabetesCanadaWebsite. 2021. Body Mass Index (BMI) Calculator - Diabetes Canada. [ONLINE] Available at: https://www.diabetes.ca/managing-my-diabetes/tools---resources/body-mass-index-(bmi)-calculator#:~:text=Body%20Mass%20Index%20is%20a,most%20adults%2018%2D65%20years. [Accessed 27 January 2021].

# Python round() Function. 2021. Python round() Function. [ONLINE] Available at: https://www.w3schools.com/python/ref_func_round.asp. [Accessed 27 January 2021].
