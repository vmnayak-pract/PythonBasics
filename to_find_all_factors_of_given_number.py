#python program to accept a number and find all the factors of that number
n=int(input("Enter an integer number"))
print("factors of",n,"are as follows")
for i in range(1,n):
    rem=n%i
    if rem==0:
      print(i)