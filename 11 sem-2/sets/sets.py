s = {1,2,3}
print(type(s))
s = {1, 1, 1, 2, 44, 5, 1, 2, 3, 5, 2, 3}
print(s)        # set don't have duplicates
l = [1, 1, 1, 1, 1, 2, 2, 2, 2, 5, 5, 5, 5, 4, 4, 4, 1, 1]
print(set(l))
# print(s[0])    indexing not possible.
s = {1, 2, 3, 5, 1}
s.add("d")      # we can append
print(s)
print(s.pop())  # pop removes random element
s.clear()
print(s)    # will print set()
s = {1, 2, 3}
t = {2, 3, 4}
print(s.intersection(t))
print(s.union(t))           # operators on set can be used
print(s.difference(t))
s.update(t)
print(s)        # union give new set, update keeps the same set.
b = set()
print(b, type(b))
# set is mutable.
b.add(123)  # in set no order is there, append adds at last but add will add any where
print(b)
b.discard(123)      # discard will remove
print(b)
b = {1, 2, 3, 4, 5}
b.remove(4)
print(b)
print(b.pop())  # removes random element
# print(b[0]) will give error no index
a = {1, 2, 3}
b = {4, 5, 6}
print(a.isdisjoint(b))  # will give True
print(a.issubset(b))
print(a.issuperset(b))
ojl=a.copy()
print(ojl)
print(id(a), id(ojl))       # here different id
op= a
print(id(op),id(a))     # here same id
op.remove(3)
print(a)        # will also remove from a
l = [1, 2, 3]
m = l
print(id(m), id(l))     # same id
m = {1,2,3}
n = set(m)
print(m, n)
