

#0 1 1 2 3 5 8


def fib(n):
    if n==0:
        return n

    # fib(n-1)
    print(n+fib(n-1), end = " ")

# fib(5)
n=5
sum = 0
for i in range(0,n):
    print(sum + sum,end = " ")
    sum+=1



