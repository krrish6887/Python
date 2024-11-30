#Programe to find Amount after adding simple intrest to principal amount 
p=int(input("Enter Principal Amount="))
r=int(input("Enter ROI per annum="))
t=int(input("Enter time period(in year)="))
A=p+(p*r*t)/100
print("TOTAL AMOUNT=",A)
