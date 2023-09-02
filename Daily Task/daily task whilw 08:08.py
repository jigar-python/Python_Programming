status=True
lucky_number=15

while status:
    number=int(input("enter the number : "))
    if number==lucky_number :
        print("the number is lucky")
        break
    else:
        print("wrong")

        
    
    choice=input("do ypou want to conmtinue ?['y/n']: ")
    if choice=='y':
        status=True
    else:
        status=False
    
