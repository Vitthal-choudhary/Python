#create a tuple which will have square of numbers from 1 to 50.
l = []
for i in range(1,51):
    l.append(i**2)
t = tuple(l)
print(t)