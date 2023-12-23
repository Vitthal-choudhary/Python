'''
1. write a program to read a text file and create another 
text file and 2 consecutive spaces ---> 1 space
'''
data_in_old = open('file.txt', 'r').read().split()
f = open('new_file.txt', 'w+')
for i in range(len(data_in_old)):
    f.write(data_in_old[i])
    f.write(" ")
    f.flush()