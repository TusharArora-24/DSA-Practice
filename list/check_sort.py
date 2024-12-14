




def check_sort(l):

    if len(l)<=1:
        return True
    
    else:
        for i in range(0,(len(l)-1)):
            # print(l[i],l[i+1])
            if l[i]<=l[i+1]:
                pass
            # print("HERE")
            # print(i+1,len(l))
            else: 
                return False
            if (i+1)==(len(l)-1):
                # print("HERE")
                return True
        # else: 
        #     return "NO"


l= [1,2,3,4,5,6]
# l= [1]
# l= [1,2,3,4,3]

if check_sort(l):
    print("YES")
else: print("NO")



