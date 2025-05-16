

def Intersection(a,b):

    m = len(a)
    n = len(b)
    i=0
    j = 0
    index = 0
    result = [0 for _ in range(min(m,n))]

    while i<m and j<n:
        print(i, j, a[i] if i < m else None, b[j] if j < n else None)
        if a[i]==b[j]:
            if index==0 or result[index-1]!=a[i]:
                result[index]=a[i]
                i+=1
                j+=1
                index+=1
            else:
                i+=1
                j+=1

        elif a[i]<b[j] :
            # print("Here")
            i+=1
        elif a[i]>b[j]:
            j+=1

    return result[:index]

a = [1,1,1,2,3]
b = [1,1,2]

print(Intersection(a,b))
