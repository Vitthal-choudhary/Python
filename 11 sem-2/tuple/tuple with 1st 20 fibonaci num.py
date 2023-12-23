#create a tuple which will have 1st 20 fibonacci numbers.
l=[]
x, y = 0, 1
l = [x,y]
for i in range(18):
    z = x+y
    x = y
    y = z
    l.append(z)
t = tuple(l)
print(t)