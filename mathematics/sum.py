# sum of n natural numbers avoiding overflow

def sum(n):
    if(n%2==0):
        return int((n/2)*(n+1))
    else: return ((n+1)/2)*n


print(int(sum(50001)))

    
