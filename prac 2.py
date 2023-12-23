import mysql.connector as connector
my_con = connector.connect(host='localhost', user='root', password='sairam', database='school')
cursor = my_con.cursor()
#cursor.execute('''create table teacher
 #                 (tid int(10) primary key, Name char(15), sub char(15)
  #                 , experience char(10), address char(40), salary int(8))''')
#my_con.commit()

cursor.execute('select address from teacher')
data = cursor.fetchall()
for i in data:
    print(i)

cursor.execute('''update teacher set salary = 25000 where experience = 0 ''')
cursor.execute('''update teacher set salary = 35000 where experience between 2 and 4 ''')
cursor.execute('''update teacher set salary = 50000 where experience = 5 ''')

my_con.commit()
my_con.close()