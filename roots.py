#calculate real roots of quadratic equation.
import math
a=int(input("Enter value of a="))
b=int(input("Enter value of b="))
c=int(input("Enter value of c="))
D=b*b-4*a*c

if(D<0):
    print("Roots are imaginary")
else:
    root1=(-b + math.sqrt(D))/(2*a)
    root2=(-b - math.sqrt(D))/(2*a)
    print(root1)
    print(root2)
