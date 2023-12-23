fil = open('poem.txt', 'r')
data = fil.read()
a = data.split(' ')


def DISPLAYWORDS(x):
    for i in x:
        if 4 > len(i) > 1 and i.isalpha():
            print(i)


DISPLAYWORDS(a)
