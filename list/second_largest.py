
def sec_largest(l):
    # using two loops O(n)
    # if len(l)<=1:
    #     return None
    # large = l[0]
    # large2 = None
    # for i in l:
    #     if large<i:
    #         large = i
    # print(large)
    # for j in l:
    #     # print(j)
    #     if j!=large:
    #         if large2 == None:
    #             large2 = j
    #         # print(j)
    #         elif large2<j:
    #             large2 = j

    # return large2


    #single traversal
    if len(l)<=1:
        return None
    
    lar = l[0]
    slar = None
    # print(lar,slar)
    for x in l[1:]:
        
        if x>lar:
            slar = lar
            lar = x
            # print(slar,lar)
        elif x<lar:
            if slar == None or slar<x:
                slar=x
    return slar



l = [2,1,1]
print(sec_largest(l))



