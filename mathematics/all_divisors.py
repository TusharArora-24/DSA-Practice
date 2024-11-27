
def get_all_divisors(n):
    
    # for i in range(1,n+1):
    #     if n%i==0:
    #         print(i, end=" ")
    
    # optimised approach
    # i=1
    # while (i*i<=n):
    #     if (n%i==0):
    #         print(i, end= " ")
    #         if(i!=n/i):
    #             print(int(n/i), end = " ")
    #     i+=1

    i = 1
    while(i*i<=n):
        if n%i == 0:
            print(i,end=" ")
        i+=1
    # print(i)
    # i-=1
    while(i>=1):
        if n%i == 0:
            # if i!=n/i:
            print(int(n/i), end = " ")
        i-=1

# get_all_divisors(25) 
def sieve(N):
    if N<=1:
        return
    isPrime = [True] * (N+1)
    
    isPrime[0] = isPrime[1] = False
    i=2
    while(i*i<N):
        if(isPrime[i]==True):
            for p in range(2*i,N+1,i):
                isPrime[p] = False
            
        i+=1
    return isPrime 


def exactly3Divisors(N):
        # code here
        
    final_div_count = 0
    isPrime = sieve(N)
    print(isPrime)
    for i in range(2,N+1):
        if(isPrime[i]==True and i*i<=N):
            final_div_count+=1

    return final_div_count
            


print(exactly3Divisors(50))
def sieve(self, limit):
        if limit <= 1:
            return []
        isPrime = [True] * (limit + 1)
        isPrime[0] = isPrime[1] = False
        i = 2
        while i * i <= limit:
            if isPrime[i]:
                for p in range(i * i, limit + 1, i):
                    isPrime[p] = False
            i += 1
        return [i for i in range(limit + 1) if isPrime[i]]

def exactly3Divisors(self, N):
    limit = int(N**0.5)
    primes = self.sieve(limit)
    
    count = 0
    for prime in primes:
        if prime * prime <= N:
            count += 1
    return count

