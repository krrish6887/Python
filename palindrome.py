#program to check of a number is palindrome

n=int(input("Enter a number="))
r=0
og=n
while(n>0):
    d=n%10
    r=(r*10)+d
    n//=10

if(r==og):
    print("number is palindrome")
else:
    print("number is not a palindorme")
