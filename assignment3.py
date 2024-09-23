"""
Assignment 3

#Challenge: Provide feedback to the user based on their BMI category (e.g., underweight, normal weight, overweight, obese).
#===============================
#Input: Prompt the user to enter their weight in kilograms and height in meters.
#Processing: Calculate the BMI using the formula: BMI = Weight / (Height^2).
#Output: Display the calculated BMI.

Placid Auguste - 9/18/2024

NOTE: This exercise was done by instructor Abdullah but, I modified it a bit
"""

# Input:
name = input("What is your name: ")
weight_input = input("Enter your weight in kilograms or pounds: ")
height_input = input("Enter your height in meters or feet: ")

# Convert Input:
weight = float(weight_input)
height = float(height_input)

# Processing:
bmi = weight / (height **2)

# Output:
txt = f"{name}, your BMI is: {bmi:.2f}"
print('\n')
print(txt)