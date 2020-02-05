lst=[]

while 1:
    item=input("enter the item:")
    lst.append(item)
    a=input("do you want to continue(y/n)")
    lst.sort(reverse=True,key=max)
        
    if a.lower()=="n":
        break
 
print(lst)
print(lst[0])


  

