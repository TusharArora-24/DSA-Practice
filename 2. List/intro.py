#basic_fucntions

l = [10,30,2,6]

# print(l)
# print(l[3])
# print(l[-1])

# l.append(54)
# print(l)

# l.insert(2,32)
# print(l)

# print(54 in l)
# print(69 in l)

# print(l.count(30))
# print(l.index(2))

# print("removal")
# l.remove(30)
# print(l)


# print(l.pop())
# print(l)

# print(l.pop(1))


# del l[1]
# print(l)

# del l[0:3]
# print(l)


# print("break")

# l.append(10)
# l.append(20)
# l.append(10)
# l.append(50)
# print(l)

# print(max(l))
# print(min(l))
# print(sum(l))

# l.reverse()
# print(l)

# l.sort()
# print(l)

# string = input("Enter elements:")

# lst = string.split()
# print(string)
# print(lst)

n = int(input("enter size:"))
lst = list(map(int, input("enter the numbers:").strip().split()))[:n]

print(lst)