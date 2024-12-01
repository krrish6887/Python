#program to check if a numbre is armstrong or not

n=int(input("Enter a number="))
digit=0
og=n
res=0
while(og>0):
    digit+=1
    og//=10
og=n
while(og>0):
    res+=pow(og%10,digit)
    og//=10

if (res==n):
    print("it is an armstrong number")
else:
    print("it is not an armstrong number")
