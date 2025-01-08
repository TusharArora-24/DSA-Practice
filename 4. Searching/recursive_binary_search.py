

def rec_bs(arr,x,low,high):
    mid = (low + (high-low))//2

    if low>high:
        return -1
    if arr[mid] == x:
        return mid + 1
    elif arr[mid]>x:
        return rec_bs(arr,x,low,high-1)
    elif arr[mid]<x:
        return rec_bs(arr,x,low+1,high)

arr = [10,10,20,30,40,40,40]
x = 20

print(rec_bs(arr,x,0,len(arr)-1))

