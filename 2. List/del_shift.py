

def deleteFromArray(arr,n,idx):
    #code here
    # del arr[idx]
    
    for i in range(idx,n):
        
        if i+1<n:
            arr[i] = arr[i+1]
        print(i,arr)
        if i==n-1:
            arr[n-1] = 0

    return arr

arr = [1,2,3,4,5,6]
n=6
idx = 2

print(deleteFromArray(arr,n,idx))




