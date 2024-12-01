#program to find prime factor of a number

n=int(input("Enter a number="))

while(n!=1):
    for i in range(1,n+1):
        if(n%i==0):
            print(i)
            n /=i
