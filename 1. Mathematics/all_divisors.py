
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




def check_prime(self,n):
        
        if n==2 or n==3:
            return True
        if n%2==0 or n%3==0:
            return False
        
        i=5
        while(i*i<=n):
            if n%i == 0 or n%(i+2)==0:
                return False
            i+=6
        return True
    
def exactly3Divisors(self,N):
    # code here
    import math
    i=2
    count=0
    while(i<=math.sqrt(N)):
        if self.check_prime(i) == True and i*i<=N:
            count+=1
        i+=1    
    return count

