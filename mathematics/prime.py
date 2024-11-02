


def prime(n):
    
    isPrime=True
    if (n==2):
        return isPrime

    else:
        for i in range(2,n):
            # print(i)
            if (n%i == 0):
                print("Here")
                isPrime = False
                return isPrime
        return isPrime


print(prime(970))












