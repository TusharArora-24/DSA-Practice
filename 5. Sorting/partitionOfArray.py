

def partition(arr,p):

    i = 0
    while i<len(arr):
        if arr[i]<arr[p]:
            if i<p:
                i+=1
            else:
                arr[p],arr[i] = arr[i],arr[p]
                p = i
                i+=1
        elif arr[p]<arr[i]:
            if i<p:
                arr[i],arr[p] = arr[p],arr[i]
                p = i
                i+=1
            else:
                i+=1
    
    print(arr)

arr = [3,8,6,7,12,10,7]
p = 2
partition(arr,p)


