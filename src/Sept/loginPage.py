class VWOLoginPage:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login_confirm(self):
        if self.email == "gau@gmail.com" and self.password == "12345":
            print("allowed")
        else:
            print("Not allowed")


email = input("Enter email ")
password = input("Enter password ")
vwo = VWOLoginPage(email, password)
vwo.login_confirm()
