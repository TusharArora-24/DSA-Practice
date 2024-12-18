


def remove_duplicates(l,n):
    # return list(set(l))
    # Naive pproach
    # u =[0] * n
    # u[0] = l[0]
    # res = 1

    # for i in range(1,n):
    #     if u[res-1]!=l[i]:
    #         # print(u)
    #         u[res] = l[i]
    #         res+=1

    # for i in range(0,n):
    #     l[i] = u[i]
    # return l

    res = 1
    for i in range(1,n):
        if l[res-1]!=l[i]:
            l[res] = l[i]
            res+=1
    print(l)
    return res


print(remove_duplicates([1,1,2,2,3,3,4,4,5,5],10))


