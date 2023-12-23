element = int(input('pop ?'))
stack = [1,2,3,4,5,6]
new_stack = []
for i in stack:
    if i != element:
        new_stack.append(i)
        stack.pop(i)
    elif i == element:
        stack.pop(i)
        for j in range(len(new_stack)):
            stack.append(new_stack[j])

print(stack, new_stack)