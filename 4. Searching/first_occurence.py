

def fo(arr,k,low,high):
    
    if low>high:
        return -1
    
    mid = (low+high)//2
    # print(arr[mid])
    if arr[mid]>k:
        return fo(arr,k,low,mid-1)
    elif arr[mid]<k:
        return fo(arr,k,mid+1,high)
    else:
        if mid == 0 or arr[mid-1]!=arr[mid]:
            return mid + 1
        else: return fo(arr,k,low,mid-1)


arr = [10,10,20,20,30,40,40,40]
x = 20

low = 0
high = len(arr)-1

print(fo(arr,x, low,high))



