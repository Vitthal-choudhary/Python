import pickle
user_to_search = input('enter id')
with open('member.dat', 'w+b') as hand:
    Member = {'S0100': 'Ashutosh', 'S0101': 'Akshat', 'S0105': 'Rohan'}
    pickle.dump(Member, hand)
    hand.seek(0)
    try:
        while True:
            data_to_read = pickle.load(hand)
            if user_to_search in data_to_read.keys():
                print(data_to_read[user_to_search])
            else:
                print('not found')
    except:
        print('end of file')

