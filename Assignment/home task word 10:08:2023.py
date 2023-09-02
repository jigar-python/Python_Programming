string=input("enter something : ")

word=input("enter a word : ")

word={}
for i in string:
    if i in word:
        word[i] += 1
    else:
        word = 1
print(f"the total frequency of woord kis :"+str(word))
