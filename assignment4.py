"""
Assignment 4

#Challenge: Implement error handling to ensure that the user enters numeric values for the coordinates.
#============================================
#Input: Prompt the user to enter the coordinates of two points in a 2D plane (x1, y1) and (x2, y2).
#Processing: Calculate the distance between the two points using the distance formula: Distance = sqrt((x2 - x1)^2 + (y2 - y1)^2).
#Output: Display the calculated distance between the two points.

Placid Auguste - 9/18/2024

NOTE: This exercise was done by instructor Abdullah but, I modified it a bit

"""

# Input:
x1 = float(input("Enter x1 coordinate "))
y1 = float(input("Enter y1 coordinate "))
x2 = float(input("Enter x2 coordinate "))
y2 = float(input("Enter y2 coordinate "))

# Formula:
x_squared = (x2 -x1) ** 2
y_squared = (y2 -y1) ** 2

# Processing:
distance_squared = x_squared + y_squared
distance = distance_squared ** 0.5

# Output:
txt = f"The distance between points is: {distance:.2f}"
print('\n')
print(txt)




