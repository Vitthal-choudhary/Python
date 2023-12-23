def bin_search(l,v,b,e):
    if b >= e:
        return -999
    mid = (b+e)/2
    if v == l[mid]:
        return mid
    elif v<l[mid]:
        e = mid
    else:
        b = mid
    return bin_search(l,v,b,e)


print(bin_search([1,2],2,3,8))