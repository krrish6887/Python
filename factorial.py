#program to find factorial of number

n=int(input("Enter a positive number="))
f=1

if(n<0):
    print("Factorial not possible")
else:
    for i in range(1,n+1):
        f*=i
    
print("Factorial=",f)
