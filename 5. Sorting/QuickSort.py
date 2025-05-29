

def Lpartition(arr,l,h):
    p = arr[h]
    i = l-1
    
    for j in range(l,h):
        if arr[j]<p:
            i+=1
            arr[j],arr[i] = arr[i],arr[j]
    arr[i+1],arr[h] = arr[h],arr[i+1]
    return i+1


def QS1(arr,l,h):
    if l<h:
        p = Lpartition(arr,l,h)
        QS1(arr,l,p-1)
        QS1(arr,p+1,h)

    return arr

# arr = [8, 4, 7, 9, 3, 10, 5]
# l,h = 0,6
# print(arr)
# print(QS1(arr,l,h))


def Hpartition(arr,l,h):
    p = arr[l]
    i = l -1
    j = h +1

    while True:
        i+=1
        while arr[i]<p:
            i+=1
        j-=1
        while arr[j]>p:
            j-=1
        if i>=j:
            return j
        arr[i],arr[j] = arr[j],arr[i]

def QS2(arr,l,h):
    if l<h:
        p = Hpartition(arr,l,h)
        QS2(arr,l,p)
        QS2(arr,p+1,h)
    return arr
arr = [8, 4, 7, 9, 3, 10, 5]
l,h = 0,6
print(arr)
print(QS2(arr,l,h))

