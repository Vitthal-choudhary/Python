import pickle
l = [(101, 'Delhi', 'Bangalore'), (102, 'Varanasi', 'Delhi'), (103, 'Jammu & Kashmir', 'Delhi')]
with open('train.dat', 'w+b') as hand:
    pickle.dump(l, hand)
    hand.seek(0)
    try:
        while True:
            data_to_read = pickle.load(hand)
            for i in range(len(data_to_read)):
                if data_to_read[i][2] == 'Delhi':
                    print(data_to_read[i])
    except:
        print('end of file')
