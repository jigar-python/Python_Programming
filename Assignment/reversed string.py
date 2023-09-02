string=input("enter the word : ")
if len(string) % 4 == 0:
    print("".join(reversed(string)))
else:
    print(string)
