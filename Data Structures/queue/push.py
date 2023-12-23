element = input('what to push')
queue = eval(input('enter queue'))


def push(arr, ele):
    arr.append(ele)
    return arr


print(push(arr=queue, ele=element))
