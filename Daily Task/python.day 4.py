a=int(input("enter the sub mark : "))

b=int(input("enter the sub mark : "))

c=int(input("enter the sub mark : "))

d=((a+b+c)/300)*100

print(d)

if d <=40 :
    print("fail")
    
elif d>=40 and d<=80 :
     print("level up")
else  :
    print("pass")
