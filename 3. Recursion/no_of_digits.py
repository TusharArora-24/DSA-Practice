

def countD(n):
    
    if n<10:
        return 1
    # if n//10:
    return 1 + countD(n//10) 

print(countD(12345))