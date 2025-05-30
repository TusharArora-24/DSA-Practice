
def func_prime(n):
    # naive approach
    # if(n==1):
    #     return False
    # if (n==2):
    #     return True
    # else:
    #     for i in range(2,n):
    #         # print(i)
    #         if (n%i == 0):
    #             return False
    #     return True
    
    # optimised approach (divisor's exist in pairs)
    
    # if (n==1):
    #     return False
    # i = 2
    # while(i*i<=n):
    #     if (n%i == 0):
    #         return False
    #     i+=1
    # return True

    # more optimised
    if n==1:
        return False
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

# print(func_prime(10333))











