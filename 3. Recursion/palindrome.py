#abba

def pal(s,i,n): 
    if n==i or n<i:
        return True
    # print(n,1)

    if s[i] == s[n-1]:
        # print(i,n-1)
        return pal(s,i+1,n-1)
    else: return False


i = 0
print(pal("abecba",i,6))
