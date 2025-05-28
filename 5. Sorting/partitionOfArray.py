

def LomutoPartition(arr,l,h):
    p = arr[h]
    i = l-1
    for j in range(l,h):
        if arr[j]<p:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    
    arr[i+1],arr[h] = arr[h],arr[i+1]
    print(arr)
    return i+1

def HoarePartition(arr,l,h):
    p = arr[l]
    i = l-1
    j = h+1
    # print(p,i,j)
    while True:
        i+=1
        # print(i)
        while arr[i]<p:
            i+=1
            # print(i)
        j-=1
        # print(j,arr[j])
        while arr[j]>p:
            j-=1
        if i>=j:
            return j
        
        arr[i],arr[j] = arr[j],arr[i]
        print(arr)
    

# arr = [3,8,6,12,10,7]
arr = [5,3,8,4,2,7,1,10]
l,h = 0,7
# print(LomutoPartition(arr,l,h))
print(HoarePartition(arr,l,h))