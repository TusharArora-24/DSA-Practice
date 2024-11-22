from prime import func_prime

def prime_fact(n):
    if n==1:
        print("1")
        return 1
    
    i = 2
    while(i*i<=n):
        # print(i,n)
        # print(i,status)
        if func_prime(i):
            if(n%i==0):
                print(i, end =' ')
                n = n/i
                continue
        i+=1

    if n>1:
        print(int(n))
prime_fact(1)