l1=[12,23,24,12,44,35,44,33,22,20]
uniquelist=[]

for i in l1:
    if i not in uniquelist:
        uniquelist.append(i)
        
print("uniquelist",uniquelist)
