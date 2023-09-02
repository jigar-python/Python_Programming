str1=input("enter the words : ")
split=str1.split()
strm = "love"
mpos = len(split) // 2
split.insert(mpos,strm)
print("new string:" + str(" ".join(split)))
