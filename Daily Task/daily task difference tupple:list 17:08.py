#List & tuple difference :

l1=[12,34,67,'hello',69,9]

print(l1)
print("before change : ",id(l1))

l1[3]=90
print(l1)
print("after change : ",id(l1))

#tuppels are immutable/unchangeable

t1=(45,65,'morning',75,8)

print("before change t1 : ",id(t1))

t1=(45,65,"abc",75,8)
print("after change t1 :",id(t1))


#difference arrAy & list
'''
array is a collection of similiar type of data elements rather
list is a collection of multiple type of data elements

'''
