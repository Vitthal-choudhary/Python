number1 = int(input("Enter a number"))
number2 = int(input("Enter a number"))
opt = input("tell the operator")
if opt == "+":
    print(number1+number2)
elif opt =="-":
    print(number1-number2)
elif opt=="*":
    print(number1*number2)
elif opt =="/":
    print(number1/number2)
else:
    print("wrong input")
