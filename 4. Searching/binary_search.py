
arr=[5,12,23,40,45,50]

x = 12


low = 0
high = len(arr) - 1


while low<=high:
    mid = (low+high)//2
    if arr[mid]==x:
        print("Found at -", mid + 1)
    elif x<arr[mid]:
        high = mid-1
    elif x>arr[mid]:
        low = mid+1
    else:
        print("Doesnt exist")

    

