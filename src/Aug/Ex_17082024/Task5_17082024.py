# ### Task #5
# - Create a program that takes two numbers as input and prints whether the first
# number is greater than, less than, or equal to the second number.

num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))
print(" 1st no.=", num1, "\n", "2nd no.=", num2)
if num1 > num2:
    print(num1, "is gretaer than", num2)
elif num1 < num2:
    print(num1, "is less than", num2)
else:
    print(num1, "and", num2, "both are equal.")
