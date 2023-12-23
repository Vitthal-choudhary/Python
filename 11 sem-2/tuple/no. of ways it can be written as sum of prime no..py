# take a no. b/w 4 and 10000 output should be no. of different ways it can be expressed as sum of 2 prime number.
x = int(input("enter a number"))
count = 0
for i in range(2, x+1):
    for j in range(2, i+1):
        if i%j==0:
            break
    if i==j:
        b = x-i
        for p in range(2, b+1):
            if b%p==0:
                break
        if p==b:
            count+=1
            print("pairs : ", i, b)
print("total possible pairs: ", count)
