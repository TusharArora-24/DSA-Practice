
def sec_largest(l):
    
    if len(l)<=1:
        return None
    large = l[0]
    large2 = 0
    for i in l:
        if large<i:
            large = i
    print(large)
    for j in l:
        # print(j)
        if j<large and large2<j:
            # print(j)
            large2 = j
    return large2

l = [20,10,20,8,12]
print(sec_largest(l))



