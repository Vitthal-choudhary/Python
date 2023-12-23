max = 0
sum = 0
count = 0
min = 0
while True:
    x=int(input("Enter a no."))
    if count==0:
        max=x
        min=x
        count += 1
    if max < x:
        max=x
    b = input("for other number press y else n")
    if min > x :
        min =x
    sum=sum+x
    if b=="n":
        break
    else:
        continue
print(max, " is the biggest no. you entered.")
print(min, "is smallest")
print("Average is ", sum/count)
ghl = input("Enter to close")