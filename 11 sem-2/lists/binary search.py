a = list(input("enter a list"))
b = int(input("enter the number whose index you want"))
begin = int(a[0])
end = int(a[len(a)-1])
while begin < end:
    mid = (begin + end)//2
    middle = int(a[mid])
    if middle == b:
        print("number found at ", mid)
        break
    elif middle < b:
        begin = mid
    else:
        end = mid
