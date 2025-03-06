

def Bsort(arr):

    n = len(arr)

    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
        
    return arr


arr = [10,4,2,5]

print(Bsort(arr))


