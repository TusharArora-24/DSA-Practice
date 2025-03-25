

def merge(arr1,arr2):

    final = []

    for i in range(0,len(arr1)):
        for j in range(0,len(arr2)):
            if arr1[i]<arr2[j]:
                final.append(arr1[i])
                break
            elif arr2[j]<arr1[i]:
                final.append(arr2[j])
                j=j+1

    print(final)

arr1 = [20,25,30]
arr2 = [11,27]

merge(arr1,arr2)




