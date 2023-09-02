len1=input("enter the string : ")

if len(len1) %4 == 0:
    print(' '.join(reversed(len1)))
else:
    print(len1)
    
