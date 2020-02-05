n=int(input())

for i in range(n):
    for k in range(n):
        if i==0 or i==n-1 or k==0 or k==n-1:
            print("*",end="")
        else:
            print(" ")
    print(" ")
