# series should be 1,-3,5,-7,9,-11........10 numbers
# make a series 1,-1,1,-1,1,-1,...
p = 1
i = 1
for j in range(10):
    i += 2
    p = p*-1
    print(p, " ", i*p)
# 1+1+2,1+2+3,1+2+3+4,....add them
a = 0
for h in range(1,5):
    for g in range(1,h+1):
        #print(h, " ", g)
        a = a+g
print(a)