
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
    while(i*i<n):
        if n%i == 0:
            print(i,end=" ")
        i+=1
    # print(i)
    i-=1
    while(i>=1):
        if n%i == 0:
            # if i!=n/i:
            print(int(n/i), end = " ")
        i-=1

get_all_divisors(30) 


def exactly3Divisors(N):
        # code here
        
    final_div_count = 0
    while(N>0):
        i=1
        count = 0
        while(i*i<N):
            if(N%i==0):
                count=count+1
            i+=1
        i-=1
        while(i>=1):
            if(N%i==0):
                count=count+1
            i-=1
        
        if count==3:
            final_div_count+=1
        print(N, count, final_div_count)
        N-=1
    return final_div_count
            


# print(exactly3Divisors(6))

