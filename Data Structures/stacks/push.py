x = input('what to push ?')
stack = [1,2,4]
top = -1
size = 10


def push(l, element):
    global stack, top
    if top == size:
        print('stack is full')
    else:
        l.append(element)
        top += 1
        top = len(l) - 1


push(stack, x)
print(stack)
