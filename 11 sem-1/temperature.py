print("For CtoF press 1 and for FtoC press 2 and 3 for CtoK")
a = int(input())
if a==1:
    C = int(input("Enter the celcius value"))
    print("Farheniet value is",9/5*C+32)
elif a==2:
    F = int(input("Enter the Farheniet value"))
    print("Celcius value is",5/9*F-32)
elif a==3:
    C = int(input("Enter the celcius value"))
    print("Kelvin value is",C+273.15)
else:
    print("Wrong input")