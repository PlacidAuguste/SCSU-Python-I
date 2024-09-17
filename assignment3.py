#Assignment 3

#Challenge: Provide feedback to the user based on their BMI category (e.g., underweight, normal weight, overweight, obese).
#===============================
#Input: Prompt the user to enter their weight in kilograms and height in meters.
#Processing: Calculate the BMI using the formula: BMI = Weight / (Height^2).
#Output: Display the calculated BMI.

#Input
weight_input = input("Enter your weight in kilograms: ")
height_input = input("Enter your height in meters: ")

#Convert Input
weight = float(weight_input)
height = float(height_input)

#Processing
bmi = weight / (height **2)

#output
print("your BMI is: ", bmi)