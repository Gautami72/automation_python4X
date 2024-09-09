# Create a program , take 2 inputs from the user num1, num2 and give them
# max
# pow num1 to num2
# sub, mul, sum, div.
# Format your out with f{""}

num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))
print("Number1:",num1)
print("Number2:",num2)
# result=max(num1, num2)
# print("Max: ", result)
print("Maximum number between",num1,"&",num2,"=",max(num1, num2))
print("Power of",num1 ,"&",num2,"=",pow(num1, num2))
print("Substraction of",num1,"&",num2,"=",(num1-num2))
print("Addition of",num1,"&",num2,"=",(num1+num2))
print("Multiplication of",num1,"&",num2,"=",(num1*num2))
print("Divison of",num1,"&",num2,"=",(num1/num2))