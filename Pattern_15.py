n=5
for i in range(n):
    for j in range(i+1):
        if(i==j or j==0 or i==4):
            print("*",end="")
        else:
            print(" ",end="")
    print()
