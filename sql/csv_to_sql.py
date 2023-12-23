import csv
import mysql.connector as connector

a = open('vitthal.csv', 'r', newline="")

data = csv.reader(a)
x = []
for i in data:
    x.append(tuple(i))
print(x)

my_con = connector.connect(host='localhost', user='root', password='sairam', database='School')
cursor = my_con.cursor()

for i in x:
    cursor.execute("insert into students values" + str(tuple(i)))
    my_con.commit()
