x = int(input("enter a number"))
if x < 10000:
    if x >= 1000:
        a = x//1000
        if a == 1:
            print("one thousand")
        elif a == 2:
            print("two thousand")
        elif a == 3:
            print("three thousand")
        elif a == 4:
            print("four thousand")
        elif a == 5:
            print("five thousand")
        elif a == 6:
            print("six thousand")
        elif a == 7:
            print("seven thousand")
        elif a == 8:
            print("eight thousand")
        elif a == 9:
            print("nine thousand")
    if x >= 100:
        b = x//100
        c = b%10
        if c==1:
            print("One hundred")
        elif c==2:
            print("two hundred")
        elif c==3:
            print("three hundred")
        elif c==4:
            print("four hundred")
        elif c==5:
            print("five hundred")
        elif c==6:
            print("Six hundred")
        elif c==7:
            print("Seven hundred")
        elif c==8:
            print("Eight hundred")
        elif c==9:
            print("Nine hundred")
    if x>=10:
        d=x//10
        e=d%10
        if e==2:
            print("Twenty")
        elif e==3:
            print("Thirty")
        elif e==4:
            print("Fourty")
        elif e==5:
            print("Fifty")
        elif e==6:
            print("Sixty")
        elif e==7:
            print("Seventy")
        elif e==8:
            print("Eighty")
        elif e==9:
            print("Ninety")
        else:
            if e==1:
                h=x%10
                if h==1:
                    print("Eleven")
                elif h==2:
                    print("twelve")
                elif h==3:
                    print("thirteen")
                elif h==4:
                    print("fourteen")
                elif h==5:
                    print("fifteen")
                elif h==6:
                    print("sixteen")
                elif h==7:
                    print("seventeen")
                elif h==8:
                    print("eighteen")
                elif h==9:
                    print("nineteen")
                elif h==0:
                    print("ten")
    if x>=1:
        d=x%10
        if d==1:
            print("one")
        elif d==2:
            print("two")
        elif d==3:
            print("three")
        elif d==4:
            print("four")
        elif d==5:
            print("five")
        elif d==6:
            print("six")
        elif d==7:
            print("seven")
        elif d==8:
            print("eight")
        elif d==9:
            print("nine")
        elif d==0:
            print()
else:
    print("wrong input.")