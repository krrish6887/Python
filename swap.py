#Programe to swap two number without using 3rd variable
a=int(input("Enter 1st number="))
b=int(input("Enter 2nd number="))
print("a =",a,"b =",b)
a=a+b
b=a-b
a=a-b
print("a =",a,"b =",b)
