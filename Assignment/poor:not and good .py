string=input("enter the sentence : ")
snot=string.find("not")
spoor=string.find("poor")
if spoor > snot and snot>0 and  spoor>0 :
    string = string.replace(string[snot :(spoor+4)],"good")
else:
    pass
print(string)
    
