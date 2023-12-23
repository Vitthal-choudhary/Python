#  n ! = n*(n-1)*(n-2)...*2*1
dfk = int(input("Enter the number whose factorial u want"))
fact = 1
for i in range(1, dfk+1):
    fact = fact*i
print(fact)  # this will give me factorial of dfk


"""# question is 2!/4! + 3!/6! +....+n!/n*2!
n = int(input("Enter a Number"))
sum = 0
f = 1
for i in range(2,n+1):
        f=f*i
#print(f)    # this is giving me factorial
g=1
for k in range(1,i*2+1):
    g=g*k # now g will give me denominator
    sum = sum + f/g
print(sum)



### New Series
### 1/2! + 3/3! + 5/4! + 7/5! + 9/6!
s = 0
b=1
for i in range(2,7):
    b = b*i
for j in range(1,10):
    if j%2!=0:
        ck = j
    s = s+ck/b
print(s)"""