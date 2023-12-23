# 1 -3 5 -7 9 ...
n=0
for i in range(1,12,2):
    n+=1
    if n%2==0:
        i *= -1
    print(i)
