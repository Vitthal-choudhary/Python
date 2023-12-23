a = int(input("Enter a number"))
for i in range(2, a+1):  # it can be 2,a/2
    if a % i == 0:  # 2 isliye liya kyoki 2 or usse agle no. se jab div karke remainder 0 dega to prime ni hoga.
        break # break bcoz not a factor
if i == a:  # we check did it go till end , if yes
    print(a, "is prime")
else:
    print("Not prime")
