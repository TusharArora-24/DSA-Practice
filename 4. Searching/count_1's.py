

def count(arr):
    
    n = len(arr)
    start = 0
    end = n-1

    while start <= end:
        
        mid = (start+end)//2
        
        if arr[mid]==0:
            # start = mid + 1
            end = mid - 1
        else:
            # if mid==0 or arr[mid-1]!=1:
            #     # print(end,mid)
            #     return ((len(arr)-1)-mid+1)
            # else:
            #     end = mid - 1
            if mid == len(arr)-1 or arr[mid+1]!=1:
                return mid + 1
            else: 
                start = mid + 1
    return 0


arr = [1 ,1 ,1 ,1, 1, 0, 0 ,0]
print(count(arr))


