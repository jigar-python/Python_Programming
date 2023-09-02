string=input("enter the value : ")

string=string.split()
i=0
count=0

while i<len(string):
    count=0
    for x in string:
        if string[i]==x:
            count=count+1
    print(string[i],"present",count,"times")
    i =i+1
         

         
    
