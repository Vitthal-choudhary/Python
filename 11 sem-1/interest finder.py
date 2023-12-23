P = int(input("Enter the Principal Value"))
R = int(input("Enter the rate"))
T = float(input("enter the time"))
a = input("S or C")
if a=="S":
    print("Simple Interest is", (P*R*T)/100)
elif  a=="C":
   print("Compound Interest is", P*(1+R/100)**T-P)
else:
    print("wrong input")
input("enter to close")
