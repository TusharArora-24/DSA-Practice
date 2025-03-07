

def SelSort(arr):

    n = len(arr)

    for i in range(n-1):
        # min = arr[i]
        print("i---",i)
        for j in range(i+1,n):
            print("j--",j)
            print("here - ",arr[i],arr[j])
            if arr[j]<arr[i]:
                arr[j],arr[i] = arr[i],arr[j]
        print(arr)
        # break

    return arr



arr = [31,20,8,15,6]

print(SelSort(arr))
