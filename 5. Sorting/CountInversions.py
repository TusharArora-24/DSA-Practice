

def CI(a,l,mid,r):

    arr1 = a[l:mid+1]
    arr2 = a[mid+1:r+1]

    m = len(arr1)
    n = len(arr2)
    i = j = 0
    count = 0
    k = l
    
    while i<m and j<n:

        if arr1[i]<arr2[j]:
            a[k] = arr1[i]
            i+=1
            k+=1
        else:
            a[k] = arr2[j]
            j+=1
            k+=1
            count = count + (len(arr1)-i)

    while i<m:
        a[k]= arr1[i]
        i+=1
        k+=1
        # count+=1

    while j<n:
        a[k]= arr2[j]
        j+=1
        k+=1
        # count+=1

    return count

    print(count)

def merge(a,l,r):
    count = 0
    if  l<r:
        
        mid = (l+r)//2
        count+=merge(a,l,mid)
        count+=merge(a,mid+1,r)
        count+=CI(a,l,mid,r)
        print(f"CI between {a[l:mid+1]} and {a[mid+1:r+1]} gives {count}")
    return count
    print(count)
a=[2,4,1,3,5]
print(merge(a,0,4))


