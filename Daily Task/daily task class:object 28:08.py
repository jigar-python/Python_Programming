class Welcome:
    def display(self):
        print('''
              1.ahmedabad
              2.mumbai
              3.delhi
              4.toronto
              5.vancouver
              ''')
class Registration:
    def input(self):
        self.a=input("enter your email :")
        self.b=input("enter your password :")
        self.c=input("confirm your password :")
class Login:
    def validate (self):
        self.x=input("enter your email :")
        self.y=input("enter your password :")
#===========flow of program==========

w1=Welcome()
r1=Registration()
l1=Login()

w1.display()
n=input("want reg ? :[Y/N] : ")
if n=="y" :
    status=True
    while(status) :
        r1.input()
        if r1.b!=r1.c:
            print("Password Incorrect")
            status=True
        else:
            print("Now login Process")
            l1.validate()
            if r1.a==l1.x and r1.b==l1.y :
                print("Login Sucessfull")
            else:
                print("Login Denied")
                status=False
else:
    print("thank you")
