#program to calculate LCM and HCF by brute force

a=int(input("Enter 1st number="))
b=int(input("Enter 2nd number="))

hcf=1
for i in range(1,min(a,b)+1):
    if(b%i == 0 and a%i == 0):
        hcf=i
print("HCF =",hcf)

lcm=(a*b)/hcf
print("LCM =",lcm)
