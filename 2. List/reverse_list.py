


def reversal(l):

    if len(l)<=1:
        return l
    # n = []
    j = len(l)-1
    for i in range(0,len(l)):
        # print(l[i])
        if i<=j:
            l[i],l[j] = l[j],l[i]
            j=j-1

    return l


    # return list(reversed(l))

print(reversal(l=[1,2,3,4,5]))





