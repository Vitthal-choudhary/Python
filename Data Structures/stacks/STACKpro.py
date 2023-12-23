class STACK:
    def __init__(self,length):
        self.stack = []
        self.top = -1
        self.length=length
        self.dis={}
        self.opr=['+', '-', '*', '/', '^']
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    
    def isEmpty(self):
        if self.stack==[]:
            return True
        else:
            return False
    
    def peek(self):     # gives the last element
        return self.stack[-1]
    
    def pop(self):
        if self.isEmpty()==False:
            self.top -= 1
            return self.stack.pop()
        else:
            print("Can't pop a empty list")
    
    def push(self, op):
        self.top += 1
        self.stack.append(op)

    def isOperand(self, ch):
        return ch.isalpha() or ch.isdigit()
    
    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            if a <= b:
                return True
            else:
                return False
        except KeyError:
            False


    def display(self):
        if self.isEmpty():
            print("Stack Empty")
        else:
            print("Updated data in the Stack:")
            print(self.peek(),"<-------TOP")
            for i in range(len(self.stack)-2,-1,-1):
                print(self.stack[i])
