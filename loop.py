#program to find sum of first 10 digit using both for and while loop in python

sum_for = 0
for i in range(11):
    sum_for += i

print("Sum using for loop:", sum_for)

sum_while = 0
i = 0
while i <= 10: 
    sum_while += i
    i += 1 

print("Sum using while loop:", sum_while)
