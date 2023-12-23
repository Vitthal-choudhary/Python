def fact(a):
    if a>=0:
        if a == 1 or a == 0:
            return 1
        else:
            return a*fact(a-1)
    else:
        return "invalid input"


o = int(input('enter  a no.'))
print(fact(o))

'''

for i in range(2, 20):
    print(fact(i))          # gives factorial of numbers from 2 to 19

'''