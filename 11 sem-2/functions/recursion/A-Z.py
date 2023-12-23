def alphabets(i):
    if i == 'Z':
        return 'Z'
    else:
        print(i)
        alphabets(chr(ord(i) + 1))


i = 'A'
alphabets(i)
print('Z')
