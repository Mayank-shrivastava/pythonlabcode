data=list(map(int,input().split()))
b=[]
for i in data:
    if i not in b:
        b.append(i)
for i in b:
    print(i,end=" ")
          



