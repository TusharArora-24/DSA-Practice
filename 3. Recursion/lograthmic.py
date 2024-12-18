
def fun(x):
    if x<=1:
        return 0
    else: return 1 + fun(x//2)

print(fun(16))

