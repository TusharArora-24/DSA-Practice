
def gccd(n1,n2):
    # naive approach
    # m = min(n1,n2)
    # for i in range(m,0,-1):
    #     if(n1%i == 0 and n2%i == 0):
    #         # print(i)
    #         hcf=i
    
    #         return hcf
    
    # euclidean approach (make both the numbers equal)
    # while n1!=n2:
    #     if n1>n2:
    #         n1=n1-n2
    #     else: n2 = n2-n1

    # return n1      

    # optimised euclidean approach (make b=0)
    if n2==0:
        return n1
    else: 
        # print(n2,n1)
        return gccd(n2,n1%n2)    

print(gccd(15,10))
