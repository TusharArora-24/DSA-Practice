

def LomutoPartition(arr,l,h):
    p = arr[h]
    i = l-1

    for j in range(l,h):
        if arr[j]<=p:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    
    arr[i+1],arr[h] = arr[h],arr[i+1]
    print(arr)
    return i+1

arr = [3,8,6,7,12,10,7]
l,h = 0,6
print(LomutoPartition(arr,l,h))