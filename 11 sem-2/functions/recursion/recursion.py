def f(x):
    print(x)
    #f(x-1) will give recursion error when we call function in that function only.
    print('sairam') # will never happen if previous statement has to execute coz previous will not complete


f(5)        # this is called recursion. Here main function is getting once only then it's copy are creating and
            # then happening.
print('hello')  # this will also not execute if f(x-1) will occur


# what i can do is :
def g(x):
    if x>0:
        print(x)
        g(x-1)
        print(x)


g(4)