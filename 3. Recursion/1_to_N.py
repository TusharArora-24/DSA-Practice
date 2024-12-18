

def series(n):
    if n==0:
        return
    
    series(n-1)
    print(n, end=" ")

series(100)
    




