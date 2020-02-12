data=list(map(int,input().split()))
b=[]
for i in data:
    if i not in b:
        b.append(i)
for i in range(len(b)-1):
    print(b[i],end="*")

print(b[len(b)-1])
    

