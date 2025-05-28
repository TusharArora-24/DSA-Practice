

def partition(arr,l,h):
    p = arr[h]
    i = l-1
    
    for j in range(l,h):
        if arr[j]<p:
            i+=1
            arr[j],arr[i] = arr[i],arr[j]
    arr[i+1],arr[h] = arr[h],arr[i+1]
    return i+1


def QS(arr,l,h):
    if l<h:
        p = partition(arr,l,h)
        QS(arr,l,p-1)
        QS(arr,p+1,h)

    return arr

arr = [8, 4, 7, 9, 3, 10, 5]
l,h = 0,6
print(arr)
print(QS(arr,l,h))
