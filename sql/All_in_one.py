import mysql.connector as connector
import csv
my_con = connector.connect(host='localhost', user='root', password='sairam', database='School')
cursor = my_con.cursor()


class play_with_data:
    def __init__(self):
        '''self.choice = int(input('add data - 1, remove data - 2, add column - 3, set values for new column - 4, store table -5'))
        if self.choice == 1:
            self.data = eval(input("enter data in form (Roll_number,'Name',class,marks,'gender')"))
            play_with_data.add_data(self, self.data)
        elif self.choice == 2:
            self.data = eval(input("enter data in form (Roll_number,'Name',class,marks,'gender')"))
            play_with_data.remove_data(self, self.data)
        elif self.choice == 3:
            self.field = input('enter field and details')
            play_with_data.add_new_column(self, self.field)
        elif self.choice == 4:
            self.field = str(input('enter "value" to set'))
            self.fielder = input('enter Roll_number')
            play_with_data.set_value(self)
        elif self.choice == 5:
            self.table = input("enter table to store")
            play_with_data.storing_sql(self, self.table)
        else:
            print('enter correct value')'''

    def add_data(self, data):
        try:
            command = "insert into students values" + str(data)
            cursor.execute(command)
            my_con.commit()
            print('data added to database')
        except connector.errors.IntegrityError:
            print("already exists can't add again")

    def remove_data(self, data):
        s = str(data[0])  # only works for primary key
        command = "delete from students where Roll_number = " + s
        cursor.execute(command)
        my_con.commit()
        print('data removed from database')

    def add_new_column(self, field):
        command = 'alter table students add(' + field + ')'
        cursor.execute(command)
        my_con.commit()
        print('new column added')

    def set_value(self):
        command = "update students set Hobby = " + self.field + " where Roll_number = " + self.fielder
        cursor.execute(command)
        my_con.commit()
        print('value set')

    def storing_sql(self, x):
        cursor.execute("select * from {}".format(x))
        data_in_database = cursor.fetchall()
        f = open('vitthal.csv', 'w')
        w = csv.writer(f)
        w.writerows(data_in_database)
        f.flush()
        f.close()


x=play_with_data()
