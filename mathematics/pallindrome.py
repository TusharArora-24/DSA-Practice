

def check_pal(n):
    rev = 0
    temp = n

    while temp!=0:
        last_d = temp%10
        rev = rev*10 + last_d
        temp = temp//10
        # breakpoint() 
    print(rev)
    return rev==n    


print(check_pal(12321))
