

def left_rotate(l):

    l[0] = l[1]
    l[1] = l[0]
    return l

print(left_rotate(l=[1,2,3,4,5]))




