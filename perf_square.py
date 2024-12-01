#program to check number is perfect square or not
import math

n=int(input("Enter a number="))
sqrt_n=math.isqrt(n)

if(sqrt_n*sqrt_n == n):
    print("Perfect Square")
else:
    print("not a Perfect Square")
