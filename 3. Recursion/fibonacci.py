

# 0 1 1 2 3 5 8


def fib(n):
    if n<=0:
        return 1

    # fib(n-1)
    return fib(n-1)+fib(n-2)

print(fib(4))   
# n=5
# sum = 0
# for i in range(0,n):
#     print(sum + sum,end = " ")
#     sum+=1
