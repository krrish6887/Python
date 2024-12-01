#program to reverse a number

n=int(input("Enter a number="))
r=0
while(n>0):
    d=n%10
    r=(r*10)+d
    n//=10

if(n<0):
    r=-r

print(r)
