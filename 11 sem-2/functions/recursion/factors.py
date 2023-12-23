# does work till 996 only
n = 1


def factors(a):
    global n
    if n <= a:          # if i do a//2 here i won't get number itself as factor.
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
