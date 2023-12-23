'''
I am                                Python
New to this             ---->       World of
World of                            New to this
Python                              I am
'''

old = open('list in correct order.dat', 'r')
new = open('list in reverse order.dat', 'w+')
data = old.readlines()
rev_data = []
for i in range(len(data)):
    rev_data.append(data.pop())

for i in range(len(rev_data)):
    x = rev_data[i].strip('\n')
    print(x)

new.writelines(rev_data)
old.close()
new.close()