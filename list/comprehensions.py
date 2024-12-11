

# l1 = [x for x in range(10) if x%2!=0]

# print(l1)


def smaller_comp(l,x):
    return {i for i in l if i<x}
    
def sep_even_odd(l):
    even = [i for i in l if i%2==0]
    odd = [i for i in l if i%2!=0]
    return even,odd
l = [1,2,3,4,5,6,7,8,9,10]
# print(smaller_comp(l,5))
even,odd = sep_even_odd(l)
# print(even,odd)


# dictionary comprehensions
l1 = [1,3,4,2,5]
d1 = {x:x**3 for x in l1}
# print(d1)


l2 = [x for x in range(1,7)]
l3 = [y for y in range(10,61,10)]

d2 = {l2[i]:l3[i] for i in range(len(l2))}


# print(d2)

d3 = dict(zip(l2,l3))
# print(d3.items())
print(d3)

d4 = {v:k for (k,v) in d3.items()}

print(d4)
