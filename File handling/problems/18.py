import pickle
data_to_add = eval(input('Enter entry in form [Book No., Book_ name, Author, Price] :-\n'))
Author = input('Author to search for')
handle = open('Book.dat', 'w+b')
l = [[101, 'Brief history of time', 'Stephen Hawking', 450],
         [102, 'Fabric of cosmos', 'Brian Greene', 380],
         [103, 'Harry Potter: Prisoner of Azkaban', 'J.K Rowling', 550],
         [104, 'Harry Potter: Goblet of Fire', 'J.K Rowling', 580],
         [105, 'String Theory: Knowing the elementary particles', 'Brian Greene', 400]]
pickle.dump(l, handle)


def CreateFile(x):
    if type(x) == list and len(x) == 4:
        pickle.dump(x, handle)
    else:
        print('cannot add')


def CountRec(a):
    if type(a) == str:
        handle.seek(0)
        try:
            while True:
                data_to_read = pickle.load(handle)
                for i in range(len(data_to_read)):
                    if Author == data_to_read[i][2]:
                        print(data_to_read[i])
        except:
            print('end of file')
    else:
        print('incorrect input')


CreateFile(data_to_add)
CountRec(Author)