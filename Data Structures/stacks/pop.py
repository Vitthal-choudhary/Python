l=[11,2,3,5]
top = -1


def pop(stack):
    global top
    if top == -1:
        print("empty")
    else:
        k = stack.pop()
        top = len(stack) - 1
        print(k)


pop(l)