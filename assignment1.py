"""
Assignment 1

Challenge: Handle cases where the user enters non-numeric input for the principal amount, interest rate, or time period, and provide appropriate error messages.
=============================
Input: Prompt the user to enter the principal amount, interest rate (in percentage), and the time period (in years).
Processing: Calculate the simple interest using the formula: Simple Interest = (Principal * Rate * Time) / 100.
Output: Display the calculated simple interest.

Placid Auguste - 9/18/2024

NOTE: This exercise was done by instructor Abdullah but, I modified it a bit
"""

# Input:
name = input("What is your name: ")
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate: "))
time = float(input("Enter the time period in years: "))

# Processing:
simple_interest = (principal * rate * time) / 100

# output:
txt = f"{name}, Your Simple Interest rate is: {simple_interest}%"
print('\n')
print(txt)
