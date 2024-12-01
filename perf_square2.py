#program to check number is perfect square or not using ceil and floor
import math

n=int(input("Enter a number="))
sqrt_n=math.sqrt(n)

if(math.floor(sqrt_n) == math.ceil(sqrt_n)):
    print("Perfect Square")
else:
    print("not a Perfect Square")
