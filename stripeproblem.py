n=int(input())
count=0
c=int(str(bin(n))[2:])
while c!=0:
    c = (c & (c<<1))
    count = count+1
    
print(count)    
