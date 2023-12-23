a = input('enter file name')
new = open('new_file.txt', 'w+')

try:
    old = open(a, 'r')
    x = old.read()
    new.write(x)
    new.flush()
except FileNotFoundError:
    print('no such file in directory')