

# sort

l = [4,1,2,6,7]

l.sort()
print(l)
l.sort(reverse=True)
print(l)

def fun(s):
    return len(s)



s = ["No","More","Excuses"]
s.sort(key=fun,reverse=True)
print(s)




class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y


def myfun(p):
    return p.x

l2 = [Point(1,15), Point(4,2), Point(3,10)]

l2.sort(key=myfun)

for i in l2:
    print(i.x)

        

ls = [69,-12,4,-40]

ms = sorted(ls,key = abs)
print(ms)

