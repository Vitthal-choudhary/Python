queue = eval(input('enter queue'))


def pop(arr):
    if len(arr) != 0:
        arr.pop(0)
        return arr


print(pop(arr=queue))
