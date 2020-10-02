#python program to find GCD of two numbers
a=int(input("Enter first number"))
b=int(input("Enter second number"))
gcd=1
i=1
while i<a and i<b:
    if a%i==0 and b%i==0:
        gcd=i
    i=i+1
print("gcd of",a,"and",b,"is",gcd)
