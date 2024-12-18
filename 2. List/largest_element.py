

def largest(l1):

    if not l1:
        return None
    else:
        l = l1[0]
        for i in l1:
            if l<i:
                l = i
        return l

l1 = [-10,-20,-15,-34,-25,-6]

print(largest(l1))







