# Task #11 -
# Fibonaci series 0,0+1, 0+1+1, n = 7 0, 1, 2, 3, 5, 8, 13

n=int(input("Enter number: "))
fibonacciSeries = [0,1]
if n>2:
	for i in range(2, n):
		nextElement = fibonacciSeries[i-1] + fibonacciSeries[i-2]
		fibonacciSeries.append(nextElement)
print(f"Fibonacci Series of {n} is {fibonacciSeries}")