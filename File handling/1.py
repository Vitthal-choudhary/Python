file = open('fox.txt','r')
print(file.read())  # reads and print full file.
print(file.read(24))    # reads and print first 24 characters
print(file.readline())  # reads first line
print(file.readlines())     # gives list of all lines as elements

file.close()

f = open('fox.txt', 'r')
print(f.tell())     # tells where the pointer is.
f.seek(10)          # i changed the pointer to 10th position
print(f.tell())

f.seek(5)
print(f.tell())
print(f.read(6))

f = open('dog.txt','w')
f.write('Hello i am dog\n')   # if something is written it will delete and add these 2 lines to it
f.write('Ashutosh is also dog\n')
f.writelines(['dog\n', 'cat\n', 'rat\n'])
f.flush()