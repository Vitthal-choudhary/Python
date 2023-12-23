l=[]
print(type(l))
l=list()
print(type(l))
# these are 3 ways to make list. last way at end
l=list("sai ram")
print(l)
l = list(input("enter a string to make it's list."))
print(l)
# if i say m=l ,then they are pointing to same thing if i do m[0]=10, it will make l = 10.
# l==m is true, their id is also same.
a = [1, 2, 3, 4]
print(a[-1])  # we can do indexing
# list is mutable
a[0] = 10025
print(a)  # now 10025 will be there instead of 1.
l = [1, 2, 3, 4]
m = l
print(m, l)
l[0] = 5
print(m, l)  # will change both.

nice_list = [j for j in range(5)]
print(nice_list)    # will give [0,1,2,3,4].
o = ['a' for j in range(3)] # will give ['a','a','a']. i can give numbers also in place of "a"
print(o)