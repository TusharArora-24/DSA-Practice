

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


# sieve(6)


def sieve2(N):

    if N<=1:
        return []
    
    isPrime = [True] * (N+1)

    isPrime[0] = isPrime[1] = False
    i=2
    while (i*i<=N):
        if isPrime[i] == True:
            for m in range(i*i,N+1,i):
                isPrime[m]=False
        i+=1
    return [i for i in range(0,N+1) if isPrime[i]==True]

def check(N):

    isPrime = sieve2(N)
    for i in isPrime:
        if i*i <=N:
            print(i*i)
        

check(30)


