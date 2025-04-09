

def msa(arr,low,mid,high):
    
    left = []
    right = []
    final = []
    i = low
    j = mid+1
    while i <= mid:
        left.append(arr[i])
        i=i+1
    while j<=high:
        right.append(arr[j])
        j=j+1
    m = 0
    n = 0

    while m<len(left) and n<len(right):
        if left[m]<right[n]:
            final.append(left[m])
            m=m+1
        else: 
            final.append(right[n])
            n=n+1
    
    while m<len(left):
        
        final.append(left[m])
        m=m+1
        
    while n<len(right):

        final.append(right[n])
        n=n+1

    # pass
    print(final)
arr = [10,15,20,11,13]
msa(arr,0,2,4)





