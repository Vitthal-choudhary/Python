'''110010  -------->    1*2^5+1*2^4+0*2^3+0*2^2+1*2^1+0*2^0   ------->     62'''
a = int(input("enter a number"))
l=[]
p=0
s=0
c=str(a)
if len(c)%3==0:
    while a!=0:
        s = s+(a%10)*(2**p)
        p+=1
        a=a//10
        if p==3:
            l.append(s)
            p=0
            s=0
    l.reverse()
    print(l)
elif len(c)%3!=0:
    ko=len(c)%3
    d = list(c)
    while len(c)%3!=0:
        d.insert(0,0)
        e=str(d)
        j=int(e)
        j+=1