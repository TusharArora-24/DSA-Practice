

def msa(arr,low,mid,high):
    
    left = arr[low:mid + 1]
    right = arr[mid+1:high+1]
    i = 0
    j = 0
    k = low
    # print(left,right)
    while i<len(left) and j<len(right):
        if left[i]<=right[j]: #for stability
            arr[k] = left[i]
            i = i+1
            k=k+1
            # print("for i---",i,arr)
        else:
            arr[k] = right[j]
            j = j+1
            k=k+1
    # print(arr)
    while i<len(left):
        # if arr[i]<arr[j]:
        arr[k] = left[i]
        i = i+1
        k=k+1
    # print(j)
    while j<len(right):
        # if arr[i]<arr[j]:
        arr[k] = right[j]
        j = j+1
        k=k+1

    print(arr)

def MS(arr,l,r):

    if l<r:
        m=(l+r)//2
        MS(arr,l,m)
        MS(arr,m+1,r)
        msa(arr,l,m,r)

    # print(arr)

arr = [10,5,30,15,7]
MS(arr,0,4)





