x = int(input("Enter the  Units."))
if x>0 and x<=50:
    print("you have to pay", x, "rupees.")
elif x>50 and x<=150:
    a = 50-(50-x)*3
    print("you have to pay", a, "rupees.")
elif x>150 and x<=300:
    b = 350+(x-150)*5
    print("you have to pay", b, "rupees.")
elif x>300 and x<=500:
    c = 1100+(x-300)*7
    print("you have to pay", c, "rupees.")
elif x>500:
    d = 2500+(x-500)*10
    print("you have to pay", d, "rupees.")
else:
    print("wrong input")


dodo = input("hit enter to close.")