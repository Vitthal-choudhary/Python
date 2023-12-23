input_from_user = input('enter the string')
upper = open('upper.txt', 'w+')
lower = open('lower.txt', 'w+')
other = open('other.txt', 'w+')
for i in input_from_user:
    if i.isupper():
        upper.write(i)
    elif i.islower():
        lower.write(i)
    else:
        other.write(i)
