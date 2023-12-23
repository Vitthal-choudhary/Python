a=int(input("Enter th date"))
if a<=3112:
    b=a//100
    j=a%100
    if b==1:
        print("1st")
    elif b==2:
        print("2nd")
    elif b==3:
        print("3rd")
    elif b==4:
        print("4th")
    elif b==5:
        print("5th")
    elif b==6:
        print("6th")
    elif b==7:
        print("7th")
    elif b==8:
        print("8th")
    elif b==9:
        print("9th")
    elif b==10:
        print("10th")
    elif b==11:
        print("11th")
    elif b==12:
        print("12th")
    elif b==13:
        print("13th")
    elif b==14:
        print("14th")
    elif b==15:
        print("15th")
    elif b==16:
        print("16th")
    elif b==17:
        print("17th")
    elif b==18:
        print("18th")
    elif b==19:
        print("19th")
    elif b==20:
        print("20th")
    elif b==21:
        print("21st")
    elif b==22:
        print("22nd")
    elif b==23:
        print("23rd")
    elif b==24:
        print("24th")
    elif b==25:
        print("25th")
    elif b==26:
        print("26th")
    elif b==27:
        print("27th")
    elif b==28:
        print("28th")
    elif b==29:
        if j==2:
            print("Wrong input")
        else:
            print("29th")
    elif b==30:
        if j==2:
            print("Wrong input")
        else:
            print("30th")
    elif b==31:
        if j==1 or j==3 or j==5 or j==7 or j==8 or j==10 or j==12:
            print("31st")
        elif j==2:
            print("Wrong input")
d = a%100
if d==1:
    print("January")
elif d==2:
    if b==29 or b==30 or b==31:
        print()
    else:
        print("february")
elif d==3:
    print("March")
elif d==4:
    print("April")
elif d==5:
    print("May")
elif d==6:
    print("june")
elif d==7:
    print("July")
elif d==8:
    print("August")
elif d==9:
    print("September")
elif d==10:
    print("October")
elif d==11:
    print("November")
elif d==12:
    print("December")
elif d>12:
    print("Wrong input")