lst1=[i for i in input().split()]
n=len(lst1)
lst2=[]
lst2.append(lst1[0])
str2=lst1[0]
for i in range(0,n):
    for j in range(1,n):
        str1=lst1[j]
        p=len(str2)
        if str2[p-1]==str1[0]:
            lst2.append(lst1[j])
            str2=str1
            lst1[j]='*'
            break
print(lst2)
