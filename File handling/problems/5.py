handle = open('poem.txt', 'r')
data = handle.read()


def AMCount(x):
    return x.count('m'), x.count('M'), x.count('a'), x.count('A')


m, M, a, A = AMCount(data)
print('m or M: ', m+M, '\na or A: ', a+A)
