# 1+1+2+1+2+3+1+2+3+4+1+2+3+4+5+.....
for i in range(10):
    for j in range(1,i+1):
        print(j,"+")


s=0
sum=0
for i in range(10):
    s=s+i                      ##here we did it using 1 loop only
    sum=sum+s
print(sum)