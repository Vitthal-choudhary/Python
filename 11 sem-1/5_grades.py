x=int(input("enter the marks"))
if x>90 and x<=100:
    print("A1 Grade")
elif x>80 and x<=90:
    print("A2 Grade")
elif x>70 and x<=80:
    print("B1 Grade")
elif x>60 and x<=50:
    print("B2 grade")
elif x>50 and x<=60:
    print("C1 Grade")
elif x>40 and x<=50:
    print("C2 Grade")
elif x>32 and x<=40:
    print("D Grade")
elif x<33:
    print("fail")
else:
    print("invalid input")