number=int(input("enter the number : "))

factorial=1

if number<0:
    print("factorial cannot be calculated for",input)

elif number==0:
    print("factorial is !")

else:
    for i in range(1,number+1):
        factorial=factorial*i
    print("factorial Is :",factorial)
    
