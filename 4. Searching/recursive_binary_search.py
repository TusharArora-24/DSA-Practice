

def rec_bs(arr,x,low,high):
    mid = (low + high)//2

    if low>high:
        return -1
    if arr[mid] == x:
        return mid + 1
    elif arr[mid]>x:
        return rec_bs(arr,x,low,high-1)
    elif arr[mid]<x:
        return rec_bs(arr,x,low+1,high)





arr = [10,15,20,30,40,50]
x = 30
low = 0
high = len(arr)-1
print(rec_bs(arr,x,low,high))



