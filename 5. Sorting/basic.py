

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
