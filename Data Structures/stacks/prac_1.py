def isEmpty(stk):
    if len(stk) == 0:
        return True
    else :
        return False

def Push(stk):
    itm = int(input("\t\tEnter the number : "))
    stk.append(itm)
    return stk
    
def Pop(stk):
    if isEmpty(stk):
        print("[!] UNDERFLOW")
    else:
        itm = stk.pop()
        print("Element popped :", itm)
        return stk

def Display(stk):
    if isEmpty(stk):
        print("[]")
        print("[!] UNDERFLOW")
    else:
        top = len(stk) - 1
        print(stk[top],"\t<-- Top")
        for i in range(2,len(stk)):
            print(stk[-i])
            
def rev_Display(stk):
    for i in range(1,len(stk)):
        print(stk[-i]*2)

