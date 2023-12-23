l=[1,2,3]
m=list(l)
n=l
print(id(l),id(m), id(n))  # they are different. but id of l,n  is  same
m[0]=100
print(m,l)  # m is changed l is same
print(l.count(2))
a=['a','b',"#",'c','d','25']  # number without comma will give error.
a.reverse()
a.sort()  # sorts on basis of ascii
a.sort(reverse=True)
print(a)
ko=['ac','ab','ac','gh','aa']
ko.sort()
print(ko)
