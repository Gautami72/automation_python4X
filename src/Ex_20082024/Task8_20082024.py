# ### Task #8
# Triangle Classifier:
# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.

side_1=int(input("Enter 1st side value:"))
side_2=int(input("Enter 1st side value:"))
side_3=int(input("Enter 1st side value:"))

if (side_1==side_2 and side_2==side_3 and side_1==side_3):
    print("It is a equilateral triangle")
elif(side_1==side_2 or side_2==side_3 or side_1==side_3):
    print("It is a isosceles triangle")
elif(side_1 !=side_2 and side_2 !=side_3 and side_1 !=side_3):
    print("It is a scalene triangle")
    