

def rem_dup(l,n):

    temp = [0]*n
    j = 0
    count = 0
    for i in range(0,len(l)):
        if i not in temp:
            
            count+=1
            j+=1
        if count>=1:
            count = 0
            print(l[i])
            temp[i] = l[i] 
    # for i in range(0,len(l)):
    #     l[i] = temp[i]
    
    return temp

l = [10,10,20,20,20,30,30]
print(rem_dup(l,7))

