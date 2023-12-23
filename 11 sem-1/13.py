x = "sairam"
print(x.islower()) # this is lower case all
x = "SAIRAM"
print(x.isupper()) # this will tell if all are upper
x = "Sairam"
print(x.isupper()) # here 1 is big so it will be false
print(x.isalpha()) # if all are alphabets
x = "1sairam23"
print(x.isalpha()) # this is mix so false
print(x.isalnum()) # this is true coz mix
a = "123"
print(a.isdigit()) # in "" they are digits
b="ert@$#"
# here alnum will aalso be false
c="   "
print(c.isspace())
c="   gh"
print(c.isspace())
x="hello"
y=x.upper() # this will make all upper
print(y)
z=y.lower()
print(z)
d=z.capitalize()
print(d)# this will make 1st letter upper case
c="         sai       "
print(c.rstrip())#this removed space from right
bkg=c.lstrip()
print(bkg)#this removes space from left but right space remains
sdk = c.strip()
print(sdk)# this removes both side spaces
a = "hello world"
v=a.lstrip("hel")
print(v)# this removes the word also from it, left or right
# also both l were removed
p = "om sai ram"
print(p.find("om"))
print(p.find('daddy')) # -1 means  it is not there in it.
print(p.count(" ")) # counts no. of spaces
