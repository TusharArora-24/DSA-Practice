

def rev(arr,start,end):
    while start<end:
        arr[start],arr[end] = arr[end],arr[start]
        start+=1
        end-=1
        
def rotateArr(arr, d):
    #Your code here
    
    lc = d%len(arr)
    
    rev(arr,0,lc-1)
    rev(arr,lc,len(arr)-1)
    rev(arr,0,len(arr)-1)




