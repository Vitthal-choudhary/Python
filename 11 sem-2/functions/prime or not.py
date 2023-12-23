def isprime(a, i):
    if a > i:
        if a % i == 0:
            return 'not prime'
    else:
        return 'prime'
    return isprime(a, i+1)


n = int(input('enter a number'))
if n == 1 or n == 0:
    print('neither prime nor composite')
else:
    i = 2
    a = isprime(n, i)
    print(a)