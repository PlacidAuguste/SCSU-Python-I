"""
Assignment 2

#Challenge: Implement error handling to ensure that the length and width entered by the user are positive numbers.
#=================================
#Input: Ask the user to enter the length and width of a rectangle.
#Processing: Calculate the area of the rectangle using the formula: Area = Length * Width.
#Output: Display the calculated area of the rectangle.

Placid Auguste - 9/18/2024
"""

# Input:
name = input("What is your name?: ")
length = float(input("Enter the length of the rectangle in inches or centimeters: "))
width = float(input("Enter the width of the rectangle in inches or centimeters: "))

# Processing:print('\n')
area = length * width

# Output:
txt = (f"{name}, The area of the rectangle is: {area:.2f}in² or {area:.2f}cm²")
print('\n')
print(txt)

