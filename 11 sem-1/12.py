'''import random
y = random.random()
print(y)  # it gives a number between 0 and 1
z = random.randint(2, 10)
print(z)'''
# 19/11/21
x = "sairam"
print(x[0])
print(x[5])
print(x[-1])
print(x[-2])
print(x[-3])
print(x[-6])
print(x[-4] == x[2])
# if i say x[0]="t" then it will be error coz string is immutable
for i in range(len(x)):
    print(x[i])
# space will also have a character
t = "sai ram"
print(t[3])

print("s"in x)
# in will tell me whether it is there or not
# we can add strings
print("Sai"+"ram")
# we can write one thing n times
print("sai"*3)

# Slicing

print(x[1:4]) # it will print 1,2,3
print(x[:5])  # start,stop,step   defaults :- 0,end,1
print(x[1:])
print(x[:])
print(x[0:-1])
# there is step in this too
print(x[0:6:2])
print(x[::-1])  #this will print opposite

a="abba"
print(a==a[::-1]) # this is palindrome

d="sairam"
print(d[:2]+d[2:])