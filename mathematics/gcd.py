
# a=9 b=12

# def gcd(a,b):
    
#     while a!=b:
#         if a>b:
#             a =a-b
#         else: b=b-a
#     return a

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
    
# def gcd(a,b):
    
#     if b == 0 :
#         return a
#     return gcd(b, a % b)

print(gcd(4,6))

