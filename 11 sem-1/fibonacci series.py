# previous 2 no. will add to give 3rd number
first = 0
second = 1
terms = int(input("Enter the terms"))
for i in range(terms):
    third = first+second
    first = second
    second = third
    print(third)