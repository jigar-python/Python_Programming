number=int(input("enter the number : "))

a=0
b=1
if number<0:
    print("the output of your input id ",a)
else:
    print(a,b,end=" ")
    for x in range (2,number):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
