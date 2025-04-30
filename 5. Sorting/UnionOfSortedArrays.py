

def UnionSort(a,b):
    m = len(a)
    n = len(b)
    i = j = 0
    index = 0

    result = [0 for _ in range(m+n)]

    while i<m and j<n:
        if a[i]<b[j]:
            if index!=0 and a[i]==result[index-1]:
                # index=index+1
                i=i+1
            else:
                result[index] = a[i]
                index=index+1
                i=i+1
        else:
            if index!=0 and b[j]==result[index-1]:
                # index=index+1
                j=j+1
            else:
                result[index] = b[j]
                j+=1
                index+=1

    while i<m:
        if index!=0 and a[i]==result[index-1]:
                # index=index+1
                i=i+1
        else:
            result[index] = a[i]
            index=index+1
            i=i+1
    while j<n:
        if index!=0 and b[j]==result[index-1]:
                # index=index+1
                j=j+1
        else:
            result[index] = b[j]
            j+=1
            index+=1
    print(result[:index])

a = [2,3,4,4,5,5,6]
b = [2,3,4]

c = a +b
c = set(sorted(c))
# print(c)
UnionSort(a,b)
