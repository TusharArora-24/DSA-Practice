
def seperate(l):

    odd = []
    even = []

    for i in range(0,len(l)):
        if l[i] % 2 == 0:
            even.append(l[i])
        else:
            odd.append(l[i])

    return odd,even

odd,even = seperate(l=[12,23,33,40,30,24]) #tuple is returned

# print(odd,even)



# l=[12,23,33,40,30,24]

# print(small(l,35))
def add(l):
    l+=[10]
# l.append([1,2,3,4])
# l1=[12,23,33,40]
# add(l)
# print(len(l))
# print(l)
# l2 = l1
# l3 = l1[:]

# print(l)
# print(l2)
# l2[0] = 2
# l3[1] = 5
# print(l1,l2,l3)
# count = 0
# for i in (l1,l2,l3):
#     # print(i[0])
#     # break
#     print("for i--", i)
#     if i[0] == 2:
#         count+=1
#     if i[1] == 5:
#         count+=10
# print(count)
l1 = [12,13]
l2 = l1
l2[0] = 2
print(l1,l2)

