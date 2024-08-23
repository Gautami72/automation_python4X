# ### Task #3
# - Explain the difference between the = operator and the == operator in Python.
# Ans--> = operator is used for assigning value to the variable.
#        == operator is used to check if both values are equal, if equal then return TRUE else FALSE.
a = int(input("Enter 1st value:"))
b = int(input("Enter 2nd value:"))
print("== Operator Result: ", a == b)

# - What does the ** operator do in Python, and how is it used?
# Ans --> This is Exponentiation operator, it will give value for 1st operand power of 2nd. eg:
res = a ** b
print("** Operator Result: ", res)

# - What does the ^ operator do in Python, and in what context is it commonly used?
# Ans --> This is Bitwise operator (XOR) & used for to set each bit to 1 if only one of two bits is 1
res = a ^ b
print("^ operator Result: ", res)
