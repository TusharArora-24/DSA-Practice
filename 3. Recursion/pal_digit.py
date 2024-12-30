

def pal(N,rev):
    
    if N==0:
        # print(N,rev)
        return rev
    
    rev = 10*rev + N%10
    # print(rev)
    return pal(N//10,rev)

rev = 0
N = 10101
if pal(N,rev) == N:
    print(True)
else: False



