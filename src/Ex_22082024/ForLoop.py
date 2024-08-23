print("########################### for loop code ########################### ")
for i in range (1,10,3):
    print(i)

for i in range(1,11):
    print("Hello->",i)

for i in range(1,5):
    print("hello")

print("########################### while loop code ########################### ")
i=0
while i<5:
    print(f"while loop: {i}", end="\n")
    i=i+1

print("########################### break code ########################### ")
for i in range(1,10):
    print(i)
    if i==5:
        break

print("\n############################")
for i in range(0,10):
    if i==6 or i==5:
        print(i)
    else:
        pass # it is use to pass

print("\n######### Even number  ###################")

for i in range(0,100):
    if i%2==0:
     print(i,end=" ")
    else:
        pass

print("\n######### continue statement  ###################")
for i in range (10):
    if i%2==0:
        continue
    else:
        print(i,end=" ")

print("\n######### Match statement  ###################")
browser_name=input("Enter browser name: ")
browser_name=browser_name.lower()
match browser_name:
    case "chrome":
        print("chrome")
    case "firefox":
        print("Firefox")
    case _:
        print("not found")

