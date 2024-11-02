#count the number of digits

def c_d(n):
    count = 0
    if n == 0:
        return 1
    else:
        while n>0:
            n = n//10
            # print(n)
            count = count + 1
        return count

print(c_d(8462))
    