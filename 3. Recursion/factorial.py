

# def fact(n):

#     if n==0:
#         return 1
#     return n*fact(n-1)

def factTR(n,a):
    if n==0:
        return a
    return (factTR(n-1,n*a))

print(factTR(0,1))
