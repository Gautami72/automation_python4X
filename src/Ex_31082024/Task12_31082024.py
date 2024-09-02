# Create a Employee Class
# A - name,age, phone, address, eid
# B - walk, talk, printdetails,
# with the Constructor which will set the values
# Ask the user about the information for E1, E2
# print the details of the E1, E2 via the print employee functions.

#Task 12
class Employee:
    name = None
    age = None
    phone = None
    address = None
    eid = None

    def __init__(self, name, age, phone, address, eid):
        print("called constructor")
        self.name = name
        self.age = age
        self.phone = phone
        self.address = address
        self.eid = eid

    def empData(self):
        print("Employee Name:", self.name)
        print("Employee Age:", self.age)
        print("Employee Phone number:", self.phone)
        print("Employee Address:", self.address)
        print("Employee Eid:", self.eid)


E1 = Employee(input("Enter name of employee"), input("Enter age of employee"),
              input("Enter Phone number of employee"), input("Enter address of employee"),
              input("Enter Eid of employee"))
E2 = Employee(input("Enter name of employee"), input("Enter age of employee"),
              input("Enter Phone number of employee"), input("Enter address of employee"),
              input("Enter Eid of employee"))

E1.empData()
E2.empData()


