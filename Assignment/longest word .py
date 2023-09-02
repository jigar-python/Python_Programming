list=[]
n=int(input("enter the list of elements : "))
for i in range (0,n):
    elements=input("enter element"+str(i+1)+ ":")
    list.append(elements)
max1=len(list[0])
temp=list[0]
for x in list :
    if (len(x)>max1):
        max1=len(x)
        temp=x
print("the longest word is ",temp)


     
