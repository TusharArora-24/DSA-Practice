

def computing_pow(x,n):

    if n==0:
        return 1
    
    temp = computing_pow(x, n // 2)

    if n%2 == 0:
        # temp = computing_pow(x, n // 2)
        return temp*temp
    
    else:
        # return temp*temp*x
        return computing_pow(x,n-1)*3
    
print(computing_pow(3,4))

