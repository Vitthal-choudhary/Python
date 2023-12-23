'''
A+B+(E-F)+(G*F)  --------->    AB+EF-+GF*+
'''

infix_expression = input('Enter the expression')
stack = ["("]
infix_expression += ")"
operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
postfix_expression = []


for i in range(len(infix_expression)):
    if infix_expression[i].isalpha():
        postfix_expression.append(infix_expression[i])
    elif infix_expression[i] == "(":
        stack.append(infix_expression[i])
    elif infix_expression[i] in operators.keys():
        order = operators[infix_expression[i]]
        while stack[-1] != '(':
            if order <= operators[stack[-1]]:
                postfix_expression.append(stack.pop())
            else:
                break
        stack.append(infix_expression[i])
    elif infix_expression[i] == ")":
        while stack[-1] != "(":
            postfix_expression.append(stack.pop())
        stack.pop()

print(postfix_expression)
