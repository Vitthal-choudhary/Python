x=input("Enter a string")
l=0 # for lower case
u=0 # for upper case
d=0 # for digits
s=0 # for spaces
o=0 # for special characters
for i in range(len(x)):
    if x[i].islower():
        l+=1
    elif x[i].isupper():
        u+=1
    elif x[i].isspace():
        s+=1
    elif x[i].isdigit():
        d+=1
    else:
        o+=1
if l>=1:
    print("No. of lower cases is ",l)
if u>=1:
    print("No. of upper cases is ",u)
if d>=1:
    print("No. of digits is ",d)
if o>=1:
    print("No. of Special Characters is ",o)
if s>=1:
    print("No. of space is ", s)