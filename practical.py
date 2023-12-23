def isEmpty(stack):
    if len(stack) == 0:
        return True
    else:
        return False


def Traversal(stack):
    if isEmpty(stack):
        print("UNDERFLOW")
    else:
        top = len(stack) - 1
        print(stack[top], "\t\t<----- Top")
        for i in range(2, len(stack) + 1):
            print(stack[-i])
        print("\n")


def Push(stack, size):
    if len(stack) == size:
        print("Overflow !!")
    else:
        itm = eval(input("Enter the tuple in form ('country name', 'capital', 'curreny') "))
        stack.append(itm)
        return stack


def Pop(stack):
    if isEmpty(stack):
        print("UNDERFLOW")
    else:
        itm = stack.pop()
        print("Element popped :", itm, "\n", "Finnaly Stack becomes :-")
        return stack


Stack = [("India", "Delhi", "Rupees"),
         ("United State Of America", "Washington D.C", "U.S Dollar"),
         ("Australia", "Cannabera", "Australian Dollar"),
         ("Canada", "Toronto", "Canadian  Dollar")]

while True:
    x = input("enter 1 to Traverse through the stack, 2 for Pushing an element, 3 for popping out an element, 4 to quit\n")
    if x == "1":
        Traversal(Stack)
    elif x == "2":
        size = 10
        a = Push(Stack, size)
        Traversal(a)
    elif x == "3":
        a = Pop(Stack)
        Traversal(a)
    elif x == "4":
        break
