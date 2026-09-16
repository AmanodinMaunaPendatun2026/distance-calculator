import math

# Input coordinates for two points
point_x1 = float(input("Enter x1: "))
point_y1 = float(input("Enter y1: "))
point_x2 = float(input("Enter x2: "))
point_y2 = float(input("Enter y2: "))

# Compute Euclidean distance using standard math library functions
distance = math.sqrt(math.pow(point_x2 - point_x1, 2) + math.pow(point_y2 - point_y1, 2))

# Display the calculated distance
print("The distance between the two points is:", round(distance, 2))

# Reflection:
# Using a library is practical because it provides ready-made functions
# such as sqrt() and pow(), making calculations easier and less repetitive.
# The math library makes the program shorter, clearer, and easier to understand.