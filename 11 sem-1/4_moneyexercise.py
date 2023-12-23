a = int(input("Enter the amount"))
b=a//2000
if b>0:
    print("You can carry", b, "notes of 2000.")
c = a-b*2000
d = c//500
if d>0:
    print("you can carry", d, "notes of 500.")
e = c-d*500
f = e//200
if f>0:
    print("You can carry", f, "notes of 200.")
g = e-f*200
h = g//100
if h>0:
    print("You can carry", h, "notes of 100.")
i = g-h*100
j = i//50
if j>0:
    print("You can carry", j, "notes of 50.")
k = i-j*50
l = k//20
if l>0:
    print("You can carry", l, "notes of 20.")
m = k-l*20
n = m//10
if n>0:
    print("You can carry", n, "notes of 10.")
o = m-n*10
p = o//5
if p>0:
    print("You can carry", p, "coins of 5.")
q = o-p*5
r = q//2
if r>0:
    print("You can carry", r, "coins of 2.")
s = q-r*2
t = s//1
if t>0:
    print("You can carry", t, "coins of 1.")
input("press enter to close.")