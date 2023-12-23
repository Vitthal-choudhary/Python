def d(b):
    c = int(input('enter a number'))
    if b != c:
        print(c)
        d(b)


e = int(input('enter number at what u want to stop'))

g = d(e)
