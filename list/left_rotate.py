

def left_rotate(l,n):

    
    if len(l)<=1:
        return "Cant be rotated"
    temp = l[0]

    for i in range(1,n):
        l[i-1] = l[i]
    
    l[n-1] = temp
    # l.append(l.pop(0))
    return l
    

print(left_rotate(l=[1,2,3,4,5],n=5))




