list = [v for v in range(1,17)]
print(list)
l = [i*2 for i in range(0,6)]   # [0,2,4,6,8,10]
print(l)
p = [num for num in range(0, 50) if num % 7 == 0]     # [0, 7, 14, 21, 28, 35, 42, 49]
print(p)
q = [num if num<5 else num*2 for num in range(2,9)]
print(q)