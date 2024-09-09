# ### Task #4
# Write a Python program to calculate the area of a circle given its radius using the formula
# ``` area=π×r^2``` ( Take pie as 3.14)
pie = 3.14
radius = float(input("Enter raduis value:"))
area = pie * pow(radius, 2)
print("Area of given circle:", area)
