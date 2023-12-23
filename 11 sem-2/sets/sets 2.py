d = {1: 'a', 2: 'b'}
print(set(d))       # gives key
print(set(d.values()))  # gives value
print(set(d.items()))   # gives set of tuple with key and values
x = {1, 2, 3}
y = {2, 4, 5}
print(x.difference_update(y))
print(x, y)
print(x.intersection_update(y))
print(x, y)
'''new function of strings'''
a = 'dog'
print('cat'.join(a), a.join('cat'), end="  ")       # adds string after each letter
#  join takes only 1 argument
print()
s = 'sairam'
print(s.split())    # makes list
print(s.split('a'))
print('*'.join(['a','b']))
l = 'abcabacb'
print(l.partition(' '))     # always give 3 parts