d1={'email':'j@gmail.com','password':'abc123'}

user_email=input("enter the email id : ")
user_password=input("enter the password : ")

if user_email == d1['email'] and user_password  == d1['password']:
    print("true")
else:
    print("false")
    
