

def sqr_rt(x):

    low = 1
    high = x//2
    ans = -1

    while low<=high:
        mid = (low+high)//2
        mid_sq = mid*mid

        if mid_sq==x:
            return mid
        elif mid_sq>x:
            high = mid -1
        else:
            low = mid+1
            ans = mid
    return ans

print(sqr_rt(10))
