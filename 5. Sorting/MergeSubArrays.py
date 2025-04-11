

def msa(arr,low,mid,high):
    
    left = arr[0:mid + 1]
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
    print(j)
    while j<len(right):
        # if arr[i]<arr[j]:
        arr[k] = right[j]
        j = j+1
        k=k+1
    # while i <= mid:
    #     left.append(arr[i])
    #     i=i+1
    # while j<=high:
    #     right.append(arr[j])
    #     j=j+1
    # m = 0
    # n = 0

    # while m<len(left) and n<len(right):
    #     if left[m]<right[n]:
    #         final.append(left[m])
    #         m=m+1
    #     else: 
    #         final.append(right[n])
    #         n=n+1
    
    # while m<len(left):
        
    #     final.append(left[m])
    #     m=m+1
        
    # while n<len(right):

    #     final.append(right[n])
    #     n=n+1


    # pass
    print(arr)
arr = [10,15,20,11,13]
msa(arr,0,2,4)





