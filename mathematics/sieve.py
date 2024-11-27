

def sieve(n):

    if(n<=1):
        return
    
    isPrime = [True] * (n+1)
    # print(isPrime)
    isPrime[0] = isPrime[1] = False
    i=2
    while(i*i<=n):

        if(isPrime[i] ==  True):
            for p in range(i*2,n+1,i):
                isPrime[p] = False
        
        i+=1
        print(isPrime)
        for i in range(2,n+1):
            if isPrime[i]:
                print(i,end = " ")


sieve(6)




