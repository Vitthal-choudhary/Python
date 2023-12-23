import pickle
with open('member.dat', 'w+b') as hand:
    Member = {'MemberNo.': 45, 'Name': 'Ashutosh'}
    pickle.dump(Member, hand)
    hand.seek(0)

