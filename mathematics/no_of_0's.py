
from factorial import fact
input_no = int(input("Enter the number"))

f = fact(input_no)
print(f"the factorial of {input_no} is - ",f )

count = 0
while f%10==0:
    f=f//10
    count+=1

print(f"the number of zeroes in {f} is - ",count )



