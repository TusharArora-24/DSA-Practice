

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
            if index!=0 and result[index-1]!=a[i]:
                result[index]=a[i]
                i+=1
                j+=1
                index+=1
                # print(result)
            elif index==0:
                result[index]=a[i]
                i+=1
                j+=1
                index+=1
                # print(result,i,j,index)
            else:
                i+=1
                j+=1

        elif a[i]<b[j] :
            # print("Here")
            i+=1
        elif a[i]>b[j]:
            j+=1

    return result[:index]

a = [1,1,3,3,3]
b = [1,1,1,1,3,5,7]

print(Intersection(a,b))
