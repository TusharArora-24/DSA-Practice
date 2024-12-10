
def bin_exp(x,n,m):

    res = 1

    while n>0:
        if n%2==1:
            # res*=x
            res = (res*x) % m 
        x= (x*x) % m
        n//=2
    return res

print(bin_exp(10,4,5))



