"""
Assignment 5
Challenge: Implement error handling to ensure that the user enters a non-negative number for the time duration.
=======================================================
Input: Prompt the user to enter a time duration in hours.
Processing: Convert the time duration to minutes and seconds.
Output: Display the converted time duration in minutes and seconds.

Placid Auguste - 9/18/2024
"""

# Input
hours = float(input("Enter time duration in hours: "))

# Processing
minutes = hours * 60
seconds = hours * 3600

# Output
txt = (f"{hours} hours is equal to {minutes} minutes or {seconds} seconds.")
print('\n')
print(txt)
