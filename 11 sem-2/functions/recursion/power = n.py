def power_to_n(x,n):
    if n == 0:
        return 1
    else:
        return x * power_to_n(x, n-1)


a = int(input('enter a number'))
b = int(input('enter the power'))
print(power_to_n(a,b))