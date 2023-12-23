# x^2/2! + x^3/3! + ... + x^n/n!
def func(x,n):
    def fact(n):
        if n == 1:
            return 1
        else:
            return n * fact(n-1)
    if n == 2:
        return (x ** n)/n
    else:
        return (x ** n)/fact(n) + func(x, n - 1)


x = int(input('enter value for x'))
n = int(input('enter value for n'))
print(func(x, n))
