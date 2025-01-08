

def fo(arr,k):

    low = 0
    high = len(arr)-1

    while low<=high:
        mid = (low + (high-low))//2
        # print(mid)
        if arr[mid]==k:
            # print(mid)
            for i in range(0,mid):
                # print(arr[i])
                if arr[i]==k:
                    
                    return i+1
            else: return mid+1

        if arr[mid]>k:
            high-=1
        else:
            low+=1
    return -1

arr = [10,10,20,20,40,40,40]
x = 10

print(fo(arr,x))



