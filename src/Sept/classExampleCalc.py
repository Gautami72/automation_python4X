class Calc:
    def sum(self, a, b):
        return a + b

    def mul(self, a, b):
        return a * b


ob1 = Calc()
a = int(input("Enter a value:"))
b = int(input("Enter B value:"))
sumres=ob1.sum(a, b)
mulres=ob1.mul(a, b)
print("Sum of A & B is", sumres)
print("Mul of A & B is", mulres)
