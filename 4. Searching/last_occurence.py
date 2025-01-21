

def last_occurence(arr,low,high,x):

    mid = (low+high)//2
    print(mid)
    while low<=high:
        print(low,high)
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x :
            high = mid - 1
        else:
            if(mid == (len(arr)-1)) or arr[mid]!=arr[mid+1]:
                return mid + 1
            else:
                low = mid + 1
    return -1


arr = [10,20,20,30,30,30,40,50,50]


print(last_occurence(arr,0,8,20))














