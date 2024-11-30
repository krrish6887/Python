#optimized program to calculate LCM and HCF

a=int(input("Enter 1st number="))
b=int(input("Enter 2nd number="))

prod=a*b

while(b%a !=0):
    c=a
    a=b%a
    b=c
    hcf=a
    
print("HCF =",hcf)

lcm=prod/hcf
print("LCM =",lcm)
