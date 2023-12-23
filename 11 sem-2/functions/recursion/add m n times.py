def d(m, n):    # m is no. of times, n is the number
    if m == 1:
        return n
    else:
        return n + d(n, m-1)


a = int(input('enter a number'))
b = int(input('enter the number of times u want to add'))
print(d(b, a))