def x():
    b=6

    def y():
        print('sai ram')     # for function y x is enclosing to y.
        a = 30
        print(a, ',', b)
        ''' first it checks if it is local if not then check in enclosing
         if not check globally, if not then check if predefined. this is LEGB Rule.'''
    y()
    # print(a)  will give error it is not defined
x()
# y() is not defined it can be called only inside x.


def z():
    a = 6

    def y():
        a = 5       # here if i give a=a+5, will give error. we can do b = a+5,print b no error.
                    # this is bcoz here i am creating new a and previous a is not defined
        print(a)
    y()
    print(a)


z()

''' function definition with default values '''
def l(p,q = 20,r=45):        # (p,20) will be error.     (q=20,p) will be wrong coz non-default value follows default value
    print(p,q,r)    # if i give print(a,b,a)    will give 1 1 1
a=1
b=2
l(a)        # will print a/p = 1 and q=20(default)
l(a,b)      # will print 1 and 2
# it prints them in same order this is called positional argumenting
l(25, r=90)     # will change r even if it's not in main function.
# can't give (r=90, 25)     coz positional argument follows key word argument.

d = 5
def g():
    global d        # I will use global d here.
    d = d+5
    print(d)        # no error


g()