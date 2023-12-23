x = input("Enter a string")
a=0
for i in range(len(x)):
    if x[i].isspace():
        a += 1
print("Number of words are : ", a+1)