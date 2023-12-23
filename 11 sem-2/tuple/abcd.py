a = ()
b = []
x=1
for i in range(ord("a"),ord("z")+1):
    b.append(chr(i)*x)
    x+=1
print(tuple(b))