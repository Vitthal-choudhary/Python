x,y,z=1,1,0
while z<500:
    z=x+y
    x=y
    y=z
    for i in range(2,z+1):
        if z%i==0:
            break
    if z==i:
        print(z,"is prime")
