status=False
class Welcome:
    def __init__(self,heet,nyc,london,mumbai):
        self.n1=heet
        self.n2=nyc
        self.n3=london
        self.n4=mumbai
    

        
    while status:
        n=input("enter you want to register:")
        if n=="y":
            print("thank you")
        else:
            print(Registration())

        

class Registration:
    def __str__(self,email,psd,cpsd):
        self.a=email
        self.b=psd
        self.cpsd
    while status:
        a=input("enter your email id:")
        b=input("enter your password:")
        c=input("confirm password:")

        if b==c:
            print("your password is success")
        else:
            print(c)
        
