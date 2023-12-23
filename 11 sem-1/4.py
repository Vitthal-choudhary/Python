x='Sai'
y='Ram'
print(x>y)
# we can compare strings on ascii
print(chr(65))
print(ord('A'))
# chr gives ascii of anyone
a = int(input("Enter a 4 digit number"))
if a<=10000:
    b = a//1000
    print(b)
    c = a//100 # // will give gint
    d = c%10 # % will give me remainder
    print(d)
    e = a//10
    f = e % 10
    print(f)
    g= a%1000
    h = g%100
    i=h%10
    print(i)
else:
    print("wrong input")
'''
x = int(input("Enter a number"))
while x > 0:
    y = x % 10
    x = x//10
    print(y, ' ', x)
# Now i can get any number how big it may be!!!
'''