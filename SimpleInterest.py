# this is a example code for simple interest
P= float(input("Please Enter the principal amount: "))
N=float(input("Please enter period in years : "))
R=float(input("Please enter the rate of interst in % p.a : "))

# calculate simple interest and total amount
I=(P*N*R)/100
A=I+P

# print the result
print(f'Simple Interest is {I:.2f} INR')
print(f'Total amount is {A:.2f} INR')