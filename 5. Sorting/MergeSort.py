

def merge(arr1,arr2):

    final = []
    m = len(arr1)
    n = len(arr2)
    i = 0
    j = 0

    while i<m and j<n:
        if arr1[i]<arr2[j]:
            final.append(arr1[i])
            i=i+1
        else:
            final.append(arr2[j])
            j=j+1
    
    while i<m:
        final.append(arr1[i])
        i=i+1
    while j<n:
        final.append(arr2[j])
        j=j+1


    print(final)

arr1 = [10, 15]
arr2 = [5, 6, 6, 30, 40]

merge(arr1,arr2)




