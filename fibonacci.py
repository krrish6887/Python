#program to know nth fibonacci series

n=int(input("Enter a number="))
a=0
b=1
nextterm=a+b
if n==1:
    print(a)
else:
    
    print(a)
    print(b)
    

for i in range(3,n+1):
    print(nextterm)
    a=b
    b=nextterm
    nextterm=a+b
