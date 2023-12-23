def hcf(a, b):
    if b == 0:
        return a
    else:
        return hcf(b, a % b)


o = int(input('enter a number'))
p = int(input('enter other number'))
print(hcf(o, p))
