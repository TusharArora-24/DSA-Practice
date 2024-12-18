
from gcd import gcd

def lcm_of_two_num(a,b):
    
    # lcm = a*b 
    # if a<b:
    #     # print(lcm,b)
    #     for i in range(lcm,b-1,-1):
    #         print(lcm,b,i)
    #         if (a%i== 0) & (b%i== 0):
    #             lcm = i
    # elif b<a:
    #     for i in range(lcm,a-1,-1):
    #         print(lcm,b,i)
    #         if (a%i== 0) & (b%i== 0):
    #             lcm = i
    # return lcm
    lcm = a*b // gcd(a,b)
    return lcm


    
# def lcm(a,b) :
#     return a * b // gcd(a,b)

print(lcm_of_two_num(4,6))

