# continue is other than break it reverses the loop
for i in range(20):
    if i>10:
        break
    elif i>5:
        continue
    print(i) # this will print till 5
print(i) # at last it will give 19
# break means it comes out of loop and come to statement out of loop
# continue will take u back to loop and do statement in loop from starting again


j=2
while j<50: # it is infinite loop
    print(j)
    j+=1
    if j>5:
        j+=2
    if j>20:
        break
print("good")
print(j)


for k in range(20):
    pass
print(k)

b=1
while b<20:
    b += 1
print(b)