#Programe to find largest between 3 numbers
a=int(input("Enter 1st number="))
b=int(input("Enter 2nd number="))
c=int(input("Enter 3rd number="))
if((a>b) and (a>c)):
    print("greatest=",a)
elif((b>a) and (b>c)):
    print("greatest=",b)
else:
    print("greatest=",c)
