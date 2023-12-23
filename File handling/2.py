import pickle

with open('dog.txt', 'w+b') as fil: # with this method close is not required
    d = {1:'a', 2:'b', 3:'c'}
    pickle.dump(d, fil)  # will add d(dict.) in fil(file)
    fil.seek(0)
    a = pickle.load(fil)
    print(a)

# this is making a copy of previous image.
f = open('cod.jpg', 'rb')
s = f.read()
# print(s)
g = open('new_cod.jpg', 'wb')
g.write(s)


# exception handling

with open('dog.txt','w+b') as fl:
    l = [1,2,3,4,5,6]
    pickle.dump(l,fl)
    fl.seek(0)
    try:
        while True:
            s = pickle.load(fl)
            print(s)
    except:
        print('end of file')
# without try and except it will give error EOFError: Ran out of input
