''' 110010  -------->    1*2^5+1*2^4+0*2^3+0*2^2+1*2^1+0*2^0   ------->     50 '''
a = int(input("Enter a number"))
decimal = 0
position = 0
while a > 0:
    decimal += ((a % 10)*(2**position))
    position += 1
    a = a//10
print(decimal)
