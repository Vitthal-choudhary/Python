"""
# read a string and print letters
a = "hello"


def letter(x,count):
    print(x[count])
    letter(x,count+1)


letter(a, 0)

# read a number and find sum of it's digits
a = 5246


def add(x):
    if x != 0:
        n=0
        c = x%10
        n+=c
        print(n)
        add((x // 10))


add(a)

"""
# palindrome


def is_palindrome(x,y,z):
    if y==z:
        is_palindrome(x,y,z-1)
    else:
        return "not palindrome"


a = input('enter string')
print(is_palindrome(a,a[0],a[(len(a)-1)]))