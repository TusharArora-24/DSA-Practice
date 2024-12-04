

def cp(self,x,N):
        
        if N == 0:
            return 1
        
        temp = self.cp(x,N//2)
        
        if N%2==0:
            return temp*temp
        else:
            return temp*temp*x
    
def termOfGP(self,A,B,N):
    #Your code here
    
    if N==1:
        return A
    
    else:
        cr = self.cp((B/A),N-1)
        # x = A*(cr)
        # N = N-1
        
    # print(cr,x,N)
    return A*(cr)

