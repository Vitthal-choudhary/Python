d = (1,2,3,4)
print(type(d))  # type tuple
print(d[0],d[3])    # indexing can be done
#d[0]=10  immutable
a = ()  #a = tuple()  this will also make empty tuple
b = (1,)    # t=(1) is int not tuple, or t=1,
t = 1,00,000    # this is not1 lakh it is tuple
print(type(t),t)    # in tuple t 3 elements are there 1,0,0
f=1,
print(id(f))
f=2,
print(id(f))    # the 2 ids will be different
k = tuple("sairam")
print(k)
j=('om','sai','ram')    # for more arguments dont use word tuple
print(type(j),j)
l=[1,2,3]
d=tuple(l)
print(d)
l=list(d)
print(l)
l = list((1,2,3,4))     # to make list of numbers u need tuple otherwise u get errors.
print(l)
a=('sai','ram')
a+=a        # we can add 2 tuples.
print(a)
print(a*3)  # print it n times
print("sai" in a)
print('sai' not in a)       # these will give true and false
t=1,1,2,2,3,4
print(min(t))       # max, min, count all can be used
print(t.count(2))   # count of 2 is 2
print(t.index(1))   # it will show index of first 1
# del a will delete tuple
d=1,2,3
print(str(d))   #prints full tuple (1,2,3)
v = d[0:2]
print(v)    #we can do slicing
d = 1,[2,3]     #it's len is 2
print(d[1])     #will print 2nd element i.e list
z=1,2,3
a,b,c=z
a,b=b,a     # this will make 213 instead of 123
print(a,b,c)    # unpacking
c=1,[2,3,4]
c[1][1]=[5,6,7]
del c[1][0]
c[1].pop()
print(c)
a = (1,2,3)
print(sum(a))
a = 1, 2, 3, 4
print(a[0:2])
b = 1, 2, 3, (4, 5, 6)
print(b[2:])
