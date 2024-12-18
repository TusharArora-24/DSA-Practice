
def findodd(arr) :
    
    res = 0 
    
    for i in arr :
        print(i,res)
        res = res ^ i 
        print(i,res)
    return res

print(findodd(arr=[4,3,4,4,5,5,3,3,3]))


