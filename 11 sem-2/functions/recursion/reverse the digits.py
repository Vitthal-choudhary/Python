def rev_digit(x):
    if x != 0:
        print(x % 10,end=" ")
        rev_digit((x // 10))


a = int(input('enter a number'))
rev_digit(a)