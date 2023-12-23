l1=['a','b','c','d','e']
del l1
#print(l1)
l2=['a','e','i','o','u']
del l2[2]
print(l2)
a="sairam"
del a
#print(a)
del l2[0:2]
print(l2)
l3=[1,2,3,4,5,6,7,8]
print(l3.pop()) # will give popped element
print(l3)
l2.pop(0)
l2.pop()
print(l2) # this has become empty list.
#now i can't pop.
l2.append(69)
print(l2)# now 69 is there in l2
l2.append([1,2,3])
print(l2[1][1])  # will give 2nd item from sub list  which is 2nd item of main list.
l2.append("hello")
mon=l2+l2
print(mon)  # this concatenates 2 lists
mon.remove(69)  # removes first occurence.
print(mon)
print(mon.index([1,2,3])) # gives first occurence of item in list
mon.insert(2,5)   # adds 5 to 3rd place
print(mon)
l3.extend(mon)  #  j=l2+l3  wil make new list but extend changes this list only
print(l3)