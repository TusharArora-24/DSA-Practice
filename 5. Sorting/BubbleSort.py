

def Bsort(arr):

    n = len(arr)

    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if swapped == False:
            print("Here")
            return arr
    return arr


arr = [20, 40, 50, 10]

print(Bsort(arr))


