# will remove the 5th list from file and put others in other file.
import pickle
with open('dog.txt','w+b') as file:
    l1 = ['ashutosh', 'XII', 23]
    l2 = ['Rohan', 'XII', 85]
    l3 = ['Akshat', 'XII', 95]
    l4 = ['Vitthal', 'XII', 99]
    l5 = ['Saketh', 'XII', 97]
    l6 = ['Rambo', 'XII', 98]
    l7 = ['Akul', 'XII', 100]
    l8 = ['Shubham Panda', 'XII', 88]
    pickle.dump(l1, file)
    pickle.dump(l2, file)
    pickle.dump(l3, file)
    pickle.dump(l4, file)
    pickle.dump(l5, file)
    pickle.dump(l6, file)
    pickle.dump(l7, file)
    pickle.dump(l8, file)
    file.seek(0)
    new_file = open('new_dog.txt', 'w+b')
    try:
        count = 0
        while True:
            s = pickle.load(file)
            print(s)
            count += 1
            if count < 5 or count>5:
                pickle.dump(s, new_file)
    except:
        print('end of first file')
    new_file.seek(0)
    try:
        while True:
            x = pickle.load(new_file)
            print(x)
    except:
        print('end of second file')
