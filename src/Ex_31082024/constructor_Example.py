class ConstDemo:
    name = None
    age = None

    def __init__(self, name, age):
        print("called, Object created:")
        self.name = name
        self.age = age

    def sleep(self, name):
        print(f"{self.name} is sleeping")


d1 = ConstDemo(name="abc", age=25)
print(d1.name)

d2 = ConstDemo(name="Rupa", age="29")
print(d2.name, d2.age)
