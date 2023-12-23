# AB+EF-+GF*+
postfix = [10,20,3,'+','*',15,'-',7,'+']
stack = []
for i in range(len(postfix)):
    if type(postfix[i]) == int:
        stack.append(postfix[i])
    elif postfix[i] == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(a+b)
    elif postfix[i] == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(a*b)
    elif postfix[i] == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(b-a)
    elif postfix[i] == '/':
        a = stack.pop()
        b = stack.pop()
        stack.append(b/a)
    elif postfix[i] == '^':
        a = stack.pop()
        b = stack.pop()
        stack.append(b**a)

print('answer = ', stack)