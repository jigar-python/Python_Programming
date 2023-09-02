import random

l1=[12,32,44,55,65,76,87,98,78,67,45,34]
computer=[12,44,65,87,67,34]
players=[32,55,76,98,78,45]

print("the number in computer : ",computer)
print("thye number in players : ",players)

random.shuffle(l1)
print(l1)

for i in l1:
    print (i)
    if i in computer:
            computer.remove(i)
            if len(computer) == 0:
                print("computer won ")
                break
    else:
        players.remove(i)
        if len(players) == 0:
            print("players won ")
            break
    print("computer items : ",computer)
    print("players items : ",players)
        
                

