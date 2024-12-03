
def cp(x,n): 
    
    if n==0:
        return 1
    
    if n%2==0:
        temp = cp(x,n//2)
        return temp*temp
    else:
        return cp(x,n-1)*x 




print(cp(7,4))