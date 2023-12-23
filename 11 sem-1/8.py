x = int(input("enter a no."))
if x>50:
    print("good")
else:
    pass

# loops are for(for fix no.),while(infinite)

for i in range(10):
    print(i)
for i in range(10,15):
    print(i,end=" ")
# For (Start stop step)
for t in range(2,10,2):
    print(t,)
for j in range(10,100,20):
    print(j,end=" ")
# step can't be negative if 10,100,-5.and also can't be 100,10,5
#but it can be 100,10,-5.
# end is necessary start is default 0 and default step is 0, step can't be fraction
for a in range(50,101,2):
    print(a,end=" ")
    a = a+5
    print(a,end=" ")
# this will first print 50 then 55 than go back to 52 then 57 and so on
for i in "sairam":
    print(i)