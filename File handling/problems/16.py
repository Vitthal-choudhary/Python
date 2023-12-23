import pickle

handle = open('COMPANY.DAT', 'wb+')
Company = {1001: ["monty", 50], 1002: ["Devu ji", 10], 1005: ["simp", 99]}
pickle.dump(Company, handle)
handle.flush()
handle.seek(0)
try:
    while True:
        data = pickle.load(handle)
        if 1005 in data:
            print(data[1005])
except:
    handle.close()
