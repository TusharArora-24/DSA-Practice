
def peakElement(arr):
    # Code here
    first = 0
    last = len(arr)-1
    if len(arr) == 1 or  len(set(arr)) == 1:
        return 0
    elif arr[0]>arr[1]:
        return 0
    elif arr[last]>arr[last - 1]:
        return last
    else:
        while (first <= last):
            
            mid = (last + first)//2
            if ((arr[mid] > arr[mid+1]) or mid == 0 ) and ((arr[mid] > arr[mid-1]) or mid == last):
                return mid
            elif mid > 0 and arr[mid-1]>arr[mid]:
                last = mid - 1
            elif arr[mid+1] > arr[mid]:
                first = mid + 1
            
    return -1


# 
# arr = [5, 5, 5, 5, 5, 5, 5]
arr = [-50, -40, -30,-10, -20, 0, 20,10]
# arr = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]
print(peakElement(arr))





