
from typing import List

def quadraticRoots(self, a : int, b : int , c:int ) -> List[int]:
        # code here
        import math
        
        D = b*b - 4*a*c
        # print(D)
        if D < 0 :
            return [-1]
        
        else:
            D = math.sqrt(D)
            # print(D)
            res1 = int((-b + D)//(2*a))
            res2 = int((-b - D)//(2*a))
            
            if res1<=res2:
                return res2,res1
            else:
                return res1,res2


