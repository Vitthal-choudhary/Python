import csv

'''# For writing -------->

f = open('csv_1.csv', 'w', newline="")   # without newline = "" 1 extra line is added in between 2 lines
write_data = csv.writer(f, delimiter="#")
s = (10, 20, 30, 'hello')
t = (40, 5, 21)
lis = [(1, 2, 3), (4, 5, 6), ('a', 'b', 'c')]
write_data.writerow(s)
write_data.writerow(t)
write_data.writerows(lis)     # puts all elements of l in different different lines.
f.close()'''

# For reading --------->

g = open('csv_1.csv', 'r')      # here newline = "" is like size, it doesn't matter
read_data = csv.reader(g, delimiter="#")
for i in read_data:
    print(i)
