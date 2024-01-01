

def bs(arr,x):

    low = 0
    high = len(arr) - 1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]==x:
            # print("Found at -", mid + 1)
            return mid
        elif x<arr[mid]:
            high = mid-1
        elif x>arr[mid]:
            low = mid+1
    return "Not Found"


arr=[5,12,23,40,45,50,55,60,65,70,75,80]

x = 800

print(bs(arr,x))

  

