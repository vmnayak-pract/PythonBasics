#python program to display sum of given series 1+1/3+1/5+...1/19
sum=0.0
for i in range(1,20,2):
    sum=sum+1/i
print("sum of series=",sum)