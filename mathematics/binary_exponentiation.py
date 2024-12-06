
def bin_exp(x,n):

    res = 1

    while n>0:
        if n%2==1:
            res*=x
        x*=x
        n//=2
    return res

print(bin_exp(10,10))



