# Task #10 -
# # Factorial n = 5 5! -->54321 -> 120 3! -> 321 -> 6 4! -> 432*1 -> 24


n=int(input("Enter number: "))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(f"Factorial of {n} is {fact}")
