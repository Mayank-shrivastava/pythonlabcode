l1=[1,3,4,2]
l2=[1,4,9,5]
b=[]
[b.append(x) for x in l2 if x not in l1]
a=l1+b

print(a)
