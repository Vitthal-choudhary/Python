"""# Factorial of a number
def fact(a):
    if a >= 0:
        if a == 1 or a == 0:
            return 1
        else:
            return a*fact(a-1)
    else:
        return "invalid input"


o = int(input('enter  a no.'))
print(fact(o))

# nth Fibonacci number


def fibonacci(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    else:
        return fibonacci(a-1)+fibonacci(a-2)


x = int(input('enter the position'))
print(fibonacci(x))
# prime or not
"""

def isprime(a, i):
    if a > i:
        if a % i == 0:
            return 'not prime'
    else:
        return 'prime'
    return isprime(a, i+1)

"""
n = int(input('enter a number'))
if n == 1 or n == 0:
    print('neither prime nor composite')
else:
    i = 2
    a = isprime(n, i)
    print(a)
"""
# sum of n prime numbers.
sum = 0
n = int(input("enter numbers"))
for i in range(n+1):
    if isprime(i,2) == "prime":
        sum += i

print(sum)
"""# factors
n = 1


def factors(a):
    global n
    if n <= a:
        if a % n == 0:
            print(n)
            n += 1
            factors(a)
        else:
            n += 1
            factors(a)


f = int(input('enter a number'))
if f > 0:
    factors(f)

# digits of a number


def dig(x):
    if x != 0:
        print(x % 10)
        dig((x // 10))

dig(125)
# reverse digits


def rev_digit(x):
    if x != 0:
        print(x % 10,end=" ")
        rev_digit((x // 10))


a = int(input('enter a number'))
rev_digit(a)
"""