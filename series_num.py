# take and print serie of numbers until 0 is entered
numbers=[]
while True:
    num=int(input("Enter a number(enter 0 to stop)="))
    
    if num==0:
        break
    numbers.append(num)

print("you entered the following numbers:")
for number in numbers:
    print(number)
