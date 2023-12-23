import csv
f = open('sports.csv', 'w+', newline='')
new_f = open('new_file.txt', 'w+')
add_data = csv.writer(f)
s = [('Events', 'Name'), ('Cricket', 'Shubham'), ('Athletics', 'Akshat'), ('Athletics', 'Akul')]
add_data.writerows(s)
f.seek(0)
read = csv.reader(f)
for i in read:
    if i[0] == 'Athletics':
        new_f.write(i[1])
        new_f.write('\n')
new_f.close()
f.close()