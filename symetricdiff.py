l1=[1,3,4,2]
l2=[1,4,9,5]
l3=[x for x in l1  if x  not in l2]
l4=[x for x in l2 if x not in l1]
print(l3+l4)

