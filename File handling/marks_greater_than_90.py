import pickle
with open('dog.txt','w+b') as file:
    l1 = ['ashutosh', 'XII', 23]
    l2 = ['Rohan', 'XII', 85]
    l3 = ['Akshat', 'XII', 95]
    l4 = ['Vitthal', 'XII', 99]
    pickle.dump(l1, file)
    pickle.dump(l2, file)
    pickle.dump(l3, file)
    pickle.dump(l4, file)
    file.seek(0)
    new_file = open('new_dog.txt', 'w+b')
    try:
        while True:
            s = pickle.load(file)
            print(s)
            if s[2] > 90:
                pickle.dump(s, new_file)
    except:
        print('end of first file')
    new_file.seek(0)
    try:
        while True:
            x = pickle.load(new_file)
            print(x)
    except:
        print('end of new file')