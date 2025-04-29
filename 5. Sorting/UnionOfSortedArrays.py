

def UnionSort(a,b):
    m = len(a)
    n = len(b)
    i = j = 0
    
    while i<m and j<n:
        if a[i]==a[i-1] :
            # c.append(a[i])
            i = i+1
            # k = k+1
            # print(c)
        elif b[j]==b[j-1] :
            # c.append(a[i])
            j = j+1

        elif a[i]<b[j]:
            print(a[i], end =" ")
            i = i+1
        elif b[j]<a[i]:
            # c.append(b[j])

            print(b[j], end =" ")
            j = j+1
        elif a[i]==b[j]:
            # c.append(a[i])
            print(a[i], end =" ")
            i = i+1
            j = j+1
            # k = k+1
            # print(c)
    while i<m :
        if a[i-1]==a[i]:
            i= i+1
        # c.append(a[i])
        else: 
            print(a[i], end =" ")
            i = i+1
        # k = k+1
        # print(c)
    while j<n: 
        if b[j-1]==b[j]:
            j=j+1
        # c.append(a[i])
        else: 
            print(b[j], end =" ")
            j=j+1
        # print(c)
    # return c

a = [2,3,4,4,5,5,6]
b = [2,3,4]

c = a +b
c = set(sorted(c))
# print(c)
UnionSort(a,b)
