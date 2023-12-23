#create 2 tuple if all elements of both tuple are same print true.
a = eval(input("enter a tuple"))
b = eval(input("enter a tuple"))
if len(a)==len(b):
    for i in range(len(a)):
        c=a[i]
        d=b[i]
    if c==d:
        print("True")
    else:
        print("False")